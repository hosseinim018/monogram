import os
import logging
import requests
from urllib.parse import urljoin
from monogram.text import format_text
from typing import Optional, Dict, Any, Union

class Network:
    """Handles network operations for Telegram API with robust error handling."""
    
    def __init__(
        self,
        token: str,
        secret_token: str,
        endpoint: str,
        proxy: bool = False,
        proxy_url: str = None,
        *args,
        **kwargs
    ) -> None:
        """
        Initialize the Network client.
        
        Args:
            token: Telegram bot token
            secret_token: Webhook verification secret
            endpoint: Telegram server endpoint (e.g., 'api.telegram.org')
            api_endpoint: Full API endpoint URL (e.g., 'https://api.telegram.org/bot<token>/')
            proxy: Whether to use proxy
            proxy_url: Proxy server URL
            session_data: Optional dict to restore requests.Session state
        """
        self.token = token
        self.secret_token = secret_token
        self.endpoint = endpoint
        self.api_endpoint = f'https://{endpoint}/bot{token}/'
        self.proxy = proxy
        self.proxy_url = proxy_url
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Configure session proxies during initialization
        if self.proxy:
            if not self.proxy_url:
                raise ValueError("Proxy URL is required when proxy is enabled.")
            proxies = {
                'http': self.proxy_url,
                'https': self.proxy_url
            }
            self.session.proxies.update(proxies)

    def download_file(
        self,
        file_path: str,
        download_path: str,
        file_name: str
    ) -> bool:
        """
        Download a file from Telegram servers.
        
        Args:
            file_path: Telegram file_path to download
            download_path: Local directory to save the file
            file_name: Name for the saved file
            
        Returns:
            bool: True if successful, False otherwise
        """
        # Construct file URL
        file_url = f"https://{self.endpoint}/file/bot{self.token}/{file_path}"
        
        try:
            # Use session proxies directly
            proxies = self.session.proxies
            
            self.logger.info(f"Downloading file from {file_url}")
            with self.session.get(file_url, stream=True, proxies=proxies) as response:
                response.raise_for_status()  # Raise HTTP errors
                
                # Create directory if missing
                os.makedirs(download_path, exist_ok=True)
                file_path = os.path.join(download_path, file_name)
                
                # Stream content to file
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:  # Filter out keep-alive chunks
                            f.write(chunk)
                
                self.logger.info(f"File saved to {file_path}")
                return True
                
        except requests.exceptions.RequestException as e:
            self.logger.error(f"File download failed: {str(e)}")
        except OSError as e:
            self.logger.error(f"File system error: {str(e)}")
        except Exception as e:
            self.logger.exception("Unexpected error during download")
        return False

    def request(
        self,
        method: str,
        payload: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        timeout: float = 10.0
    ) -> Optional[requests.Response]:
        """
        Execute Telegram API request with error handling.
        
        Args:
            method: Telegram API method (e.g., 'sendMessage')
            payload: Dictionary of API parameters
            files: Files to upload (multipart/form-data)
            return_response: Whether to return response object
            
        Returns:
            Response object if return_response=True, None otherwise
        """
        url = urljoin(self.api_endpoint, method)
        payload = self._prepare_payload(payload)
        # print(f"Requesting {url} with payload: {payload} and files: {files}")

        try:
            self.logger.info(f"Request to {method} with payload: {payload}")
            
            response = self.session.post(
                url,
                data=payload,
                files=files,
                timeout=timeout
            )
            response.raise_for_status()  # Raise HTTP errors
            
            # Log Telegram API errors
            json_resp = response.json()
            if not json_resp.get('ok', False):
                self.logger.error(f"Telegram API error: {json_resp.get('description')}")
                return json_resp['result'] if return_response else None
              
            self.logger.info(f"Request successful ({response.status_code})")
            return json_resp['result'] if return_response else None
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {str(e)}")
            if return_response and hasattr(e, 'response'):
                return e.response
        except ValueError as e:
            self.logger.error(f"JSON parsing error: {str(e)}")
        except Exception as e:
            self.logger.exception("Unexpected API request error")
        
        finally:
            # Ensure response is closed if not returned
            if response and not return_response:
                response.close()
    
    def _prepare_payload(self, raw_payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepares a payload dictionary for Telegram API requests.
        Removes None values and formats text/caption fields.

        Args:
            raw_payload: The dictionary of parameters for the API method.

        Returns:
            A cleaned and formatted payload dictionary.
        """
        if raw_payload:
            # Remove None values from payload
            payload = {k: v for k, v in raw_payload.items() if v is not None}

            if 'self' in payload:
                payload.pop('self')
            if 'cls' in payload:
                payload.pop('cls')
            if 'kwargs' in payload:
                payload.pop('kwargs')
            # Apply text formatting if 'text' or 'caption' keys exist
            if 'text' in payload and payload['text'] is not None:
                payload['text'] = format_text(payload['text'])
            if 'caption' in payload and payload['caption'] is not None:
                payload['caption'] = format_text(payload['caption'])
                
            return payload
        return {}