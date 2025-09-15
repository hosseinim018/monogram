from typing import Optional, Dict, Any, Union, List
from monogram.text import format_text
from monogram.monoTypes import ChatMember, File, InputFile, Message
from .network import Network
import requests
import json
import logging



class Methods(Network):
    def __init__(
        self,
        token: str,
        secret_token: str,
        endpoint: str,
        proxy: bool,
        proxy_url: str,
    ):
        """
        Initialize the Methods class with connection parameters.
        
        Args:
            token: Authentication token for API access
            secret_token: Secret token for additional security
            endpoint: Base endpoint URL for the service
            proxy: Whether to use proxy
            proxy_url: Proxy server URL (if proxy is enabled)
        """

        super().__init__(
            token=token,
            secret_token=secret_token,
            endpoint=endpoint,
            proxy=proxy,
            proxy_url=proxy_url,
        )

    def sendMessage(
        self,
        chat_id: Union[int, str],
        text: str,
        parse_mode: Optional[str] = 'html',
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Send a text message to a specified chat.

        Args:
            chat_id: Unique identifier for the target chat
            text: Text of the message to be sent
            parse_mode: Formatting mode (Markdown/HTML)
            reply_markup: Additional interface options
            return_response: Whether to return the raw response object
            **kwargs: Additional API parameters

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If required parameters are missing
            requests.exceptions.RequestException: For request errors
        """
        # Validate required parameters
        if not chat_id:
            raise ValueError("chat_id is required")
        if not text.strip():
            raise ValueError("text cannot be empty")

        # Prepare base message payload
        payload = {
            'chat_id': chat_id,
            'text': format_text(text),
            'parse_mode': parse_mode,
            'reply_markup': reply_markup,
            **kwargs
        }

        # Remove None values to avoid sending null parameters
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        # Serialize JSON-compatible values
        if isinstance(clean_payload.get('reply_markup'), dict):
            clean_payload['reply_markup'] = json.dumps(clean_payload['reply_markup'])

        try:
            result =  self.request(
                method="sendMessage",
                payload=clean_payload,
                return_response=return_response
            )
            return Message(**result)
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send message to chat {chat_id}")
            raise  # Re-raise the exception for caller handling

    def setWebhook(
        self,
        url: str,
        certificate: Optional[Union[str, bytes]] = None,
        ip_address: Optional[str] = None,
        max_connections: Optional[int] = None,
        allowed_updates: Optional[list[str]] = None,
        drop_pending_updates: Optional[bool] = None,
        secret_token: Optional[str] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Specify a URL and receive incoming updates via an outgoing webhook.

        Args:
            url: HTTPS URL to send updates to. Use an empty string to remove webhook.
            certificate: Public key certificate so that the Telegram servers can verify the
                         authenticity of a webhook. Can be a path to a file or file content.
            ip_address: The fixed IP address which will be used to send webhook requests instead of
                        resolving the webhook URL's host.
            max_connections: The maximum allowed number of simultaneous HTTPS connections to the webhook
                             for incoming updates. Defaults to 40.
            allowed_updates: A JSON-serialized list of the update types you want your bot to receive.
                             For example, ["message", "edited_channel_post", "callback_query"].
                             Specify an empty list to receive all update types except
                             chat_member, message_reaction, message_reaction_count, and chat_boost.
                             If not specified, all update types will be received.
            drop_pending_updates: Pass True to drop all pending updates.
            secret_token: A secret token to be sent in a header “X-Telegram-Bot-Api-Secret-Token”
                          in every webhook request, 1-256 characters.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If the 'url' parameter is missing.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not url:
            raise ValueError("url is a required parameter for setWebhook.")

        payload = {
            'url': url,
            'ip_address': ip_address,
            'max_connections': max_connections,
            'drop_pending_updates': drop_pending_updates,
            'secret_token': secret_token,
            **kwargs
        }

        # Handle allowed_updates as a JSON-serialized list
        if allowed_updates is not None:
            payload['allowed_updates'] = json.dumps(allowed_updates)

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        files = {}
        if certificate:
            if isinstance(certificate, str): # Assume it's a file path
                try:
                    files['certificate'] = open(certificate, 'rb')
                except FileNotFoundError:
                    logging.error(f"Certificate file not found at: {certificate}")
                    raise
            elif isinstance(certificate, bytes): # Assume it's file content
                files['certificate'] = ('certificate.pem', certificate, 'application/x-pem-file')
            else:
                raise TypeError("Certificate must be a file path (str) or file content (bytes).")

        try:
            # If files are present, requests will automatically set the Content-Type to multipart/form-data
            # For JSON data, we should use 'data' instead of 'json' for requests.post when 'files' is also used.
            # We'll need to send the payload as a dictionary of strings, not json=...
            if files:
                # Convert non-file payload items to strings for multipart/form-data
                data_payload = {k: str(v) for k, v in clean_payload.items()}
                response = self.request(
                    method="setWebhook",
                    payload=data_payload, # Pass as data, not json
                    return_response=return_response,
                    files=files # Pass files separately
                )
            else:
                response = self.request(
                    method="setWebhook",
                    payload=clean_payload, # Pass as JSON
                    return_response=return_response
                )
            return response
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set webhook for URL: {url}. Error: {e}")
            raise
        finally:
            # Ensure file handles are closed if opened
            if 'certificate' in files and hasattr(files['certificate'], 'close'):
                files['certificate'].close()

    def deleteWebhook(
        self,
        drop_pending_updates: Optional[bool] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Remove webhook integration.

        Args:
            drop_pending_updates: Pass True to drop all pending updates.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            requests.exceptions.RequestException: For request-related errors.
        """
        payload = {
            'drop_pending_updates': drop_pending_updates,
            **kwargs
        }
        
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="deleteWebhook",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to delete webhook. Error: {e}")
            raise

    def getWebhookInfo(
        self,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Get current webhook status.

        Args:
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions (though this method usually has none).

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            requests.exceptions.RequestException: For request-related errors.
        """
        payload = {**kwargs} # No specific parameters for getWebhookInfo, but allow kwargs
        try:
            return self.request(
                method="getWebhookInfo",
                payload=payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get webhook information. Error: {e}")
            raise

    def answerCallbackQuery(
        self,
        callback_query_id: str,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Send answers to callback queries sent from inline keyboards. The answer will be displayed
        to the user as a notification at the top of the chat screen or as an alert.

        Args:
            callback_query_id: Unique identifier for the query to be answered.
            text: Text of the notification. If not specified, a default "answered" text is shown.
                  1-200 characters.
            show_alert: If True, an alert will be shown by the client instead of a notification at the
                        top of the chat screen. Defaults to False.
            url: URL that will be opened by the user's client. If you have created a Game object via
                 BotFather, you can use a game URL.
            cache_time: The maximum amount of time in seconds that the result of the callback query
                        may be cached client-side. Telegram apps will not request the same callback
                        query again for at least this many seconds. Defaults to 0.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If 'callback_query_id' is missing or empty.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not callback_query_id:
            raise ValueError("callback_query_id is required for answerCallbackQuery.")

        payload = {
            'callback_query_id': callback_query_id,
            'text': format_text(text),
            'show_alert': show_alert,
            'url': url,
            'cache_time': cache_time,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="answerCallbackQuery",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to answer callback query {callback_query_id}. Error: {e}")
            raise

    def approveChatJoinRequest(
            self,
            chat_id: Union[int, str],
            user_id: Union[int, str],
            return_response: bool = True,
            **kwargs: Any
        ) -> Optional[requests.Response]:
            """
            Use this method to approve a chat join request. The bot must be an administrator
            in the chat for this to work and must have the can_invite_users administrator right.

            Args:
                chat_id: Unique identifier for the target chat or username of the target channel
                        (in the format @channelusername).
                user_id: Unique identifier of the user whose join request is to be approved.
                return_response: Whether to return the raw response object.
                **kwargs: Additional API parameters for future extensions.

            Returns:
                requests.Response if return_response=True, None otherwise

            Raises:
                ValueError: If 'chat_id' or 'user_id' is missing or empty.
                requests.exceptions.RequestException: For request-related errors.
            """
            if not chat_id:
                raise ValueError("chat_id is required for approveChatJoinRequest.")
            if not user_id:
                raise ValueError("user_id is required for approveChatJoinRequest.")

            payload = {
                'chat_id': chat_id,
                'user_id': user_id,
                **kwargs
            }

            # Remove None values from the payload
            clean_payload = {k: v for k, v in payload.items() if v is not None}

            try:
                return self.request(
                    method="approveChatJoinRequest",
                    payload=clean_payload,
                    return_response=return_response
                )
            except requests.exceptions.RequestException as e:
                logging.error(f"Failed to approve chat join request for chat {chat_id}, user {user_id}. Error: {e}")
                raise

    def banChatMember(
        self,
        chat_id: Union[int, str],
        user_id: Union[int, str],
        until_date: Optional[Union[int, str]] = None,
        revoke_messages: Optional[bool] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to ban a user in a group, a supergroup or a channel.
        In a supergroup or channel, the user will be able to return to the chat
        if they unblock the bot. Returns True on success.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            user_id: Unique identifier of the target user.
            until_date: Date when the user will be unbanned, Unix time. If user is banned for
                        more than 366 days or less than 30 seconds from the current time,
                        they are considered to be banned forever.
            revoke_messages: Pass True to delete all messages from the chat for the user
                             and restrict them from sending any message in the chat for
                             the duration of the ban.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If 'chat_id' or 'user_id' is missing or empty.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for banChatMember.")
        if not user_id:
            raise ValueError("user_id is required for banChatMember.")

        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            'until_date': until_date,
            'revoke_messages': revoke_messages,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="banChatMember",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to ban chat member {user_id} in chat {chat_id}. Error: {e}")
            raise

    def banChatSenderChat(
        self,
        chat_id: Union[int, str],
        sender_chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to ban a channel chat in a supergroup or a channel.
        Until the chat is unbanned, the owner of the banned chat will not be able to
        send messages and join live streams on behalf of the channel in the supergroup
        or channel. The bot must be an administrator in the chat for this to work and
        must have the appropriate administrator rights.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            sender_chat_id: Unique identifier of the target sender chat.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If 'chat_id' or 'sender_chat_id' is missing or empty.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for banChatSenderChat.")
        if not sender_chat_id:
            raise ValueError("sender_chat_id is required for banChatSenderChat.")

        payload = {
            'chat_id': chat_id,
            'sender_chat_id': sender_chat_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="banChatSenderChat",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to ban sender chat {sender_chat_id} in chat {chat_id}. Error: {e}")
            raise
    
    def closeForumTopic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to close an open topic in a forum supergroup chat. The bot must be
        an administrator in the chat for this to work and must have the can_manage_topics
        administrator rights, unless it is the creator of the topic.

        Args:
            chat_id: Unique identifier for the target chat (supergroup username or ID).
            message_thread_id: Unique identifier for the target message thread of the forum topic.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If 'chat_id' or 'message_thread_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for closeForumTopic.")
        if not isinstance(message_thread_id, int) or message_thread_id <= 0:
            raise ValueError("message_thread_id must be a positive integer for closeForumTopic.")

        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="closeForumTopic",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to close forum topic {message_thread_id} in chat {chat_id}. Error: {e}")
            raise
    
    def closeGeneralForumTopic(
        self,
        chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to close an open General forum topic a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have
        the can_manage_topics administrator rights.

        Args:
            chat_id: Unique identifier for the target chat (supergroup username or ID).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for closeGeneralForumTopic.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="closeGeneralForumTopic",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to close general forum topic in chat {chat_id}. Error: {e}")
            raise

    def copyMessage(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = 'html',
        caption_entities: Optional[list[Dict[str, Any]]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to copy messages of any kind. Service messages and invoice messages
        can't be copied. The method is analogous to the method forwardMessage, but the
        copied message doesn't have a link to the original message.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            from_chat_id: Unique identifier for the chat where the original message was sent
                          (or channel username in the format @channelusername).
            message_id: Message identifier in the chat specified in from_chat_id.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            caption: New caption for media, 0-1024 characters after entities parsing. If not specified,
                     the original caption is kept.
            parse_mode: Mode for parsing entities in the new caption.
            caption_entities: A JSON-serialized list of special entities that appear in the caption,
                              which can be specified instead of parse_mode.
            disable_notification: Sends the message silently. Users will receive a notification with no sound.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            reply_markup: A JSON-serialized object for an inline keyboard, custom reply keyboard,
                          or a reply keyboard remove_keyboard or force_reply.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If 'chat_id', 'from_chat_id', or 'message_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for copyMessage.")
        if not from_chat_id:
            raise ValueError("from_chat_id is required for copyMessage.")
        if not isinstance(message_id, int) or message_id <= 0:
            raise ValueError("message_id must be a positive integer for copyMessage.")

        payload = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id,
            'message_thread_id': message_thread_id,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'reply_parameters': reply_parameters,
            'reply_markup': reply_markup,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        # Serialize JSON-compatible values if they are dictionaries/lists
        if isinstance(clean_payload.get('reply_markup'), dict):
            clean_payload['reply_markup'] = json.dumps(clean_payload['reply_markup'])
        if isinstance(clean_payload.get('reply_parameters'), dict):
            clean_payload['reply_parameters'] = json.dumps(clean_payload['reply_parameters'])
        if isinstance(clean_payload.get('caption_entities'), list):
            clean_payload['caption_entities'] = json.dumps(clean_payload['caption_entities'])

        try:
            return self.request(
                method="copyMessage",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to copy message {message_id} from chat {from_chat_id} to chat {chat_id}. Error: {e}")
            raise
    
    def createChatInviteLink(
        self,
        chat_id: Union[int, str],
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to create an additional invite link for a chat.
        The bot must be an administrator in the chat for this to work and must have
        the can_invite_users administrator rights.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            name: Invite link name; 1-32 characters.
            expire_date: Point in time (Unix timestamp) when the link will expire.
            member_limit: The maximum number of users that can join the chat via the invite link.
                          0-99999.
            creates_join_request: True, if users joining the chat via the link need to be approved by
                                  the chat administrators.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            The response object will contain a ChatInviteLink object on success.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for createChatInviteLink.")

        payload = {
            'chat_id': chat_id,
            'name': name,
            'expire_date': expire_date,
            'member_limit': member_limit,
            'creates_join_request': creates_join_request,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="createChatInviteLink",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to create chat invite link for chat {chat_id}. Error: {e}")
            raise

    def createForumTopic(
        self,
        chat_id: Union[int, str],
        name: str,
        icon_color: Optional[int] = None,
        icon_custom_emoji_id: Optional[str] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to create a topic in a forum supergroup chat. The bot must be
        an administrator in the chat for this to work and must have the can_manage_topics
        administrator rights.

        Args:
            chat_id: Unique identifier for the target chat (supergroup username or ID).
            name: Topic name, 1-128 characters.
            icon_color: Color of the topic icon in RGB format. Currently only 7 colors are allowed:
                        0x6FB9F0 (blue), 0xFFD67E (yellow), 0xCB86EE (purple), 0xFF93B2 (red),
                        0xK6EE9B (green), 0xFCB69C (pink), 0x229ED9 (dark blue).
            icon_custom_emoji_id: Unique identifier of the custom emoji shown as the topic icon.
                                  Use getForumTopicIconStickers to get all available forum topic
                                  icon stickers.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns a Message object on success, which will have the message_id
            of the created topic's "opening message".

        Raises:
            ValueError: If 'chat_id' or 'name' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for createForumTopic.")
        if not name or not isinstance(name, str) or not (1 <= len(name) <= 128):
            raise ValueError("name must be a string between 1 and 128 characters for createForumTopic.")

        payload = {
            'chat_id': chat_id,
            'name': name,
            'icon_color': icon_color,
            'icon_custom_emoji_id': icon_custom_emoji_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="createForumTopic",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to create forum topic '{name}' in chat {chat_id}. Error: {e}")
            raise

    def declineChatJoinRequest(
        self,
        chat_id: Union[int, str],
        user_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to decline a chat join request. The bot must be an administrator
        in the chat for this to work and must have the can_invite_users administrator right.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            user_id: Unique identifier of the user whose join request is to be declined.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If 'chat_id' or 'user_id' is missing or empty.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for declineChatJoinRequest.")
        if not user_id:
            raise ValueError("user_id is required for declineChatJoinRequest.")

        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="declineChatJoinRequest",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to decline chat join request for chat {chat_id}, user {user_id}. Error: {e}")
            raise
    
    def deleteChatPhoto(
        self,
        chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to delete a chat photo. Photos can't be changed for private chats.
        The bot must be an administrator in the chat for this to work and must have
        the can_delete_messages administrator right.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for deleteChatPhoto.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="deleteChatPhoto",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to delete chat photo for chat {chat_id}. Error: {e}")
            raise

    def deleteChatStickerSet(
        self,
        chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to delete a group sticker set from a supergroup.
        The bot must be an administrator in the chat for this to work and must have
        the can_edit_other_messages administrator right.

        Args:
            chat_id: Unique identifier for the target chat (supergroup username or ID).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for deleteChatStickerSet.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="deleteChatStickerSet",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to delete chat sticker set for chat {chat_id}. Error: {e}")
            raise
    
    def deleteForumTopic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to delete a forum topic in a forum supergroup chat. The bot must be
        an administrator in the chat for this to work and must have the can_delete_messages
        administrator rights.

        Args:
            chat_id: Unique identifier for the target chat (supergroup username or ID).
            message_thread_id: Unique identifier for the target message thread of the forum topic.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If 'chat_id' or 'message_thread_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for deleteForumTopic.")
        if not isinstance(message_thread_id, int) or message_thread_id <= 0:
            raise ValueError("message_thread_id must be a positive integer for deleteForumTopic.")

        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="deleteForumTopic",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to delete forum topic {message_thread_id} in chat {chat_id}. Error: {e}")
            raise
    
    def deleteMyCommands(
        self,
        scope: Optional[Dict[str, Any]] = None,
        language_code: Optional[str] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to delete the list of the bot's commands for the given scope and user language.
        After deletion, higher level commands will be active. If the scope is omitted, default
        bot commands will be deleted.

        Args:
            scope: A JSON-serialized object describing the scope of commands to delete.
                   Defaults to BotCommandScopeDefault.
            language_code: A two-letter ISO 639-1 language code. If empty, commands will be
                           applied to all users from the given scope, for whose language
                           there are no dedicated commands.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            requests.exceptions.RequestException: For request-related errors.
        """
        payload = {
            'scope': scope,
            'language_code': language_code,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        # Serialize JSON-compatible values if they are dictionaries
        if isinstance(clean_payload.get('scope'), dict):
            clean_payload['scope'] = json.dumps(clean_payload['scope'])

        try:
            return self.request(
                method="deleteMyCommands",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to delete bot commands. Scope: {scope}, Language Code: {language_code}. Error: {e}")
            raise
    
    def editChatInviteLink(
        self,
        chat_id: Union[int, str],
        invite_link: str,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to edit a non-primary invite link created by the bot.
        The bot must be an administrator in the chat for this to work and must have
        the can_invite_users administrator rights.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            invite_link: The invite link to edit.
            name: Invite link name; 1-32 characters.
            expire_date: Point in time (Unix timestamp) when the link will expire.
            member_limit: The maximum number of users that can join the chat via the invite link.
                          0-99999.
            creates_join_request: True, if users joining the chat via the link need to be approved by
                                  the chat administrators.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            The response object will contain a ChatInviteLink object on success.

        Raises:
            ValueError: If 'chat_id' or 'invite_link' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for editChatInviteLink.")
        if not invite_link:
            raise ValueError("invite_link is required for editChatInviteLink.")

        payload = {
            'chat_id': chat_id,
            'invite_link': invite_link,
            'name': name,
            'expire_date': expire_date,
            'member_limit': member_limit,
            'creates_join_request': creates_join_request,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="editChatInviteLink",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to edit chat invite link {invite_link} for chat {chat_id}. Error: {e}")
            raise

    def editForumTopic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int,
        name: Optional[str] = None,
        icon_custom_emoji_id: Optional[str] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to edit the name and icon of a topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have
        the can_manage_topics administrator rights, unless it is the creator of the topic.

        Args:
            chat_id: Unique identifier for the target chat (supergroup username or ID).
            message_thread_id: Unique identifier for the target message thread of the forum topic.
            name: New topic name, 1-128 characters.
            icon_custom_emoji_id: Unique identifier of the custom emoji shown as the topic icon.
                                  Use getForumTopicIconStickers to get all available forum topic
                                  icon stickers. Pass an empty string to remove the icon.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If 'chat_id' or 'message_thread_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for editForumTopic.")
        if not isinstance(message_thread_id, int) or message_thread_id <= 0:
            raise ValueError("message_thread_id must be a positive integer for editForumTopic.")
        
        # At least one of 'name' or 'icon_custom_emoji_id' must be provided
        if name is None and icon_custom_emoji_id is None:
            raise ValueError("At least 'name' or 'icon_custom_emoji_id' must be provided for editForumTopic.")
        if name is not None and not (1 <= len(name) <= 128):
            raise ValueError("name must be a string between 1 and 128 characters if provided for editForumTopic.")

        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'name': name,
            'icon_custom_emoji_id': icon_custom_emoji_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="editForumTopic",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to edit forum topic {message_thread_id} in chat {chat_id}. Error: {e}")
            raise

    def editGeneralForumTopic(
        self,
        chat_id: Union[int, str],
        name: str,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to edit the name of the General forum topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have
        the can_manage_topics administrator rights.

        Args:
            chat_id: Unique identifier for the target chat (supergroup username or ID).
            name: New topic name, 1-128 characters.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise

        Raises:
            ValueError: If 'chat_id' or 'name' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for editGeneralForumTopic.")
        if not name or not isinstance(name, str) or not (1 <= len(name) <= 128):
            raise ValueError("name must be a string between 1 and 128 characters for editGeneralForumTopic.")

        payload = {
            'chat_id': chat_id,
            'name': name,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="editGeneralForumTopic",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to edit general forum topic name in chat {chat_id}. Error: {e}")
            raise

    def exportChatInviteLink(
        self,
        chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to generate a new primary invite link for a chat; any previously
        generated primary invite link is revoked. The bot must be an administrator in the chat
        for this to work and must have the can_invite_users administrator rights.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the new invite link as a string.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for exportChatInviteLink.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="exportChatInviteLink",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to export chat invite link for chat {chat_id}. Error: {e}")
            raise

    def forwardMessage(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to forward messages of any kind. Service messages can't be forwarded.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            from_chat_id: Unique identifier for the chat where the original message was sent
                          (or channel username in the format @channelusername).
            message_id: Message identifier in the chat specified in from_chat_id.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            disable_notification: Sends the message silently. Users will receive a notification with no sound.
            protect_content: Protects the contents of the forwarded message from forwarding and saving.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the sent Message.

        Raises:
            ValueError: If 'chat_id', 'from_chat_id', or 'message_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for forwardMessage.")
        if not from_chat_id:
            raise ValueError("from_chat_id is required for forwardMessage.")
        if not isinstance(message_id, int) or message_id <= 0:
            raise ValueError("message_id must be a positive integer for forwardMessage.")

        payload = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id,
            'message_thread_id': message_thread_id,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="forwardMessage",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to forward message {message_id} from chat {from_chat_id} to chat {chat_id}. Error: {e}")
            raise

    def getChat(
        self,
        chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to get up-to-date information about the chat (current name of the chat,
        description, picture, etc.). Returns a Chat object on success.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions (though this method usually has none).

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns a Chat object.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for getChat.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="getChat",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get chat information for chat {chat_id}. Error: {e}")
            raise

    def getChatAdministrators(
        self,
        chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to get a list of administrators in a chat, which aren't bots.
        Returns an Array of ChatMember objects.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns an Array of ChatMember objects.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for getChatAdministrators.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="getChatAdministrators",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get chat administrators for chat {chat_id}. Error: {e}")
            raise

    def getChatMember(
        self,
        chat_id: Union[int, str],
        user_id: int,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to get information about a member of a chat.
        Returns a ChatMember object on success.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            user_id: Unique identifier of the target user.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns a ChatMember object.

        Raises:
            ValueError: If 'chat_id' or 'user_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for getChatMember.")
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("user_id must be a positive integer for getChatMember.")

        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            response =  self.request(
                method="getChatMember",
                payload=clean_payload,
                return_response=return_response
            )
            if response:
                return ChatMember(**response)
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get chat member {user_id} for chat {chat_id}. Error: {e}")
            raise
    
    def getChatMemberCount(
        self,
        chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to get the number of members in a chat.
        Returns Int on success.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the number of members as an integer.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for getChatMemberCount.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="getChatMemberCount",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get chat member count for chat {chat_id}. Error: {e}")
            raise
    
    def getChatMenuButton(
        self,
        chat_id: Optional[int] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to get the current value of the bot's menu button in a private chat,
        or the default menu button. Returns a MenuButton object on success.

        Args:
            chat_id: Unique identifier for the target private chat. If not specified, default
                     bot's menu button will be returned.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns a MenuButton object.

        Raises:
            requests.exceptions.RequestException: For request-related errors.
        """
        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="getChatMenuButton",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get chat menu button for chat {chat_id}. Error: {e}")
            raise

    def getFile(
        self,
        file_id: str,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to get basic info about a file and prepare it for downloading.
        For the moment, currently only photos and audio files can be downloaded via this method.
        The file can then be downloaded via the link `https://api.telegram.org/file/bot<token>/<file_path>`,
        where `<file_path>` is taken from the response. It is guaranteed that the link will be valid
        for at least 1 hour. When the link expires, a new one can be requested by calling getFile again.

        Args:
            file_id: File identifier to get information about.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns a File object.

        Raises:
            ValueError: If 'file_id' is missing or empty.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not file_id:
            raise ValueError("file_id is required for getFile.")

        payload = {
            'file_id': file_id,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            response =  self.request(
                method="getFile",
                payload=clean_payload,
                return_response=return_response
            )
            if response:
                response['bot'] = self
                return File(**response)
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get file information for file_id {file_id}. Error: {e}")
            raise

    def getForumTopicIconStickers(
        self,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to get custom emoji stickers, which can be used as a forum topic icon
        by the method createForumTopic. Requires no parameters.

        Args:
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions (though this method usually has none).

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns an Array of Sticker objects.

        Raises:
            requests.exceptions.RequestException: For request-related errors.
        """
        payload = {**kwargs} # This method typically takes no parameters, but allow kwargs for future proofing

        # Remove None values from the payload (likely empty for this method)
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="getForumTopicIconStickers",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get forum topic icon stickers. Error: {e}")
            raise

    def getMe(
        self,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        A simple method for testing your bot's authentication token.
        Requires no parameters. Returns a User object on success.

        Args:
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions (though this method usually has none).

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns a User object.

        Raises:
            requests.exceptions.RequestException: For request-related errors.
        """
        payload = {**kwargs} # This method takes no parameters, but allow kwargs for future proofing

        # Remove None values from the payload (likely empty for this method)
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="getMe",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get bot information (getMe). Error: {e}")
            raise

    def getMyCommands(
        self,
        scope: Optional[Dict[str, Any]] = None,
        language_code: Optional[str] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to get the current list of the bot's commands for the given scope and user language.
        If commands aren't set for the given scope and language code, an empty list is returned.
        If the scope is omitted, default bot commands are returned.

        Args:
            scope: A JSON-serialized object describing the scope of commands.
                   Defaults to BotCommandScopeDefault.
            language_code: A two-letter ISO 639-1 language code or an empty string.
                           If empty, commands will be applied to all users from the given scope,
                           for whose language there are no dedicated commands.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns an Array of BotCommand objects.

        Raises:
            requests.exceptions.RequestException: For request-related errors.
        """
        payload = {
            'scope': scope,
            'language_code': language_code,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        # Serialize JSON-compatible values if they are dictionaries
        if isinstance(clean_payload.get('scope'), dict):
            clean_payload['scope'] = json.dumps(clean_payload['scope'])

        try:
            return self.request(
                method="getMyCommands",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get bot commands. Scope: {scope}, Language Code: {language_code}. Error: {e}")
            raise

    def getMyDefaultAdministratorRights(
        self,
        for_channels: Optional[bool] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to get the current default administrator rights of the bot.

        Args:
            for_channels: Pass True to get default administrator rights of the bot in channels.
                          Otherwise, default administrator rights of the bot in groups and supergroups will be returned.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns a ChatAdministratorRights object.

        Raises:
            requests.exceptions.RequestException: For request-related errors.
        """
        payload = {
            'for_channels': for_channels,
            **kwargs
        }

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="getMyDefaultAdministratorRights",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get default administrator rights (for_channels={for_channels}). Error: {e}")
            raise

    def getMyDescription(
        self,
        language_code: Optional[str] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to get the current bot description for the given user language.
        If no language code is specified, the default bot description will be returned.

        Args:
            language_code: A two-letter ISO 639-1 language code or an empty string.
                           For example, 'en' for English or 'es' for Spanish.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns a BotDescription object.

        Raises:
            requests.exceptions.RequestException: For request-related errors.
        """
        payload = {
            'language_code': language_code,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="getMyDescription",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get bot description for language code '{language_code}'. Error: {e}")
            raise
    
    def getMyName(
        self,
        language_code: Optional[str] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to get the current bot name for the given user language.
        If no language code is specified, the default bot name will be returned.

        Args:
            language_code: A two-letter ISO 639-1 language code or an empty string.
                           For example, 'en' for English or 'es' for Spanish.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns a BotName object.

        Raises:
            requests.exceptions.RequestException: For request-related errors.
        """
        payload = {
            'language_code': language_code,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="getMyName",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get bot name for language code '{language_code}'. Error: {e}")
            raise

    def getMyShortDescription(
        self,
        language_code: Optional[str] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to get the current bot short description for the given user language.
        If no language code is specified, the default bot short description will be returned.

        Args:
            language_code: A two-letter ISO 639-1 language code or an empty string.
                           For example, 'en' for English or 'es' for Spanish.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns a BotShortDescription object.

        Raises:
            requests.exceptions.RequestException: For request-related errors.
        """
        payload = {
            'language_code': language_code,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="getMyShortDescription",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get bot short description for language code '{language_code}'. Error: {e}")
            raise

    def getUserProfilePhotos(
        self,
        user_id: int,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to get a user's profile pictures. Returns a UserProfilePhotos object.

        Args:
            user_id: Unique identifier of the target user.
            offset: Sequential number of the first photo to get. By default, 0 is used.
            limit: Limits the number of photos to be retrieved. Values between 1-100 are accepted.
                   Defaults to 100.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns a UserProfilePhotos object.

        Raises:
            ValueError: If 'user_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("user_id must be a positive integer for getUserProfilePhotos.")

        payload = {
            'user_id': user_id,
            'offset': offset,
            'limit': limit,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="getUserProfilePhotos",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get user profile photos for user ID {user_id}. Error: {e}")
            raise

    def hideGeneralForumTopic(
        self,
        chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to hide the General forum topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have
        the can_manage_topics administrator rights. The topic will be automatically
        unhidden if no other topics are at least one non-hidden topic is present.

        Args:
            chat_id: Unique identifier for the target chat (supergroup username or ID).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for hideGeneralForumTopic.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="hideGeneralForumTopic",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to hide general forum topic in chat {chat_id}. Error: {e}")
            raise

    def leaveChat(
        self,
        chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method for your bot to leave a group, supergroup or channel.
        Returns True on success.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for leaveChat.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="leaveChat",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to leave chat {chat_id}. Error: {e}")
            raise

    def pinChatMessage(
        self,
        chat_id: Union[int, str],
        message_id: int,
        disable_notification: Optional[bool] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to add a message to the list of pinned messages in a chat.
        If the message was already pinned, it will be moved to the top of the list.
        The bot must be an administrator in the chat for this to work and must have
        the can_pin_messages administrator right in the supergroup or channel.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            message_id: Identifier of a message to pin.
            disable_notification: Pass True if it is not necessary to send a notification to
                                  all chat members about the new pinned message. Notifications
                                  are always disabled in channels and private chats.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If 'chat_id' or 'message_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for pinChatMessage.")
        if not isinstance(message_id, int) or message_id <= 0:
            raise ValueError("message_id must be a positive integer for pinChatMessage.")

        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            'disable_notification': disable_notification,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="pinChatMessage",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to pin message {message_id} in chat {chat_id}. Error: {e}")
            raise
    def promoteChatMember(
        self,
        chat_id: Union[int, str],
        user_id: int,
        is_anonymous: Optional[bool] = None,
        can_manage_chat: Optional[bool] = None,
        can_delete_messages: Optional[bool] = None,
        can_manage_video_chats: Optional[bool] = None,
        can_restrict_members: Optional[bool] = None,
        can_promote_members: Optional[bool] = None,
        can_change_info: Optional[bool] = None,
        can_invite_users: Optional[bool] = None,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to promote or demote a user in a supergroup or a channel.
        The bot must be an administrator in the chat for this to work and must have
        the can_promote_members administrator right.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            user_id: Unique identifier of the target user.
            is_anonymous: Pass True if the administrator's presence in the chat should be hidden.
            can_manage_chat: Pass True if the administrator can access the chat event log,
                             chat statistics, message statistics in channels, see channel
                             members names, see anonymous administrators in supergroups and
                             do everything that a normal member can do.
            can_delete_messages: Pass True if the administrator can delete messages of other users.
            can_manage_video_chats: Pass True if the administrator can manage voice chats.
            can_restrict_members: Pass True if the administrator can restrict, ban or unban chat members.
            can_promote_members: Pass True if the administrator can add new administrators with a subset
                                 of their own privileges or demote administrators that it has promoted.
            can_change_info: Pass True if the administrator can change the chat title, photo and other settings.
            can_invite_users: Pass True if the administrator can create invite links and invite new users to the chat.
            can_post_messages: Pass True if the administrator can post messages in the channel (channels only).
            can_edit_messages: Pass True if the administrator can edit messages of other users and their own messages (channels only).
            can_pin_messages: Pass True if the administrator can pin messages.
            can_manage_topics: Pass True if the administrator can manage topics in supergroups (forum supergroups only).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If 'chat_id' or 'user_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for promoteChatMember.")
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("user_id must be a positive integer for promoteChatMember.")

        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            'is_anonymous': is_anonymous,
            'can_manage_chat': can_manage_chat,
            'can_delete_messages': can_delete_messages,
            'can_manage_video_chats': can_manage_video_chats,
            'can_restrict_members': can_restrict_members,
            'can_promote_members': can_promote_members,
            'can_change_info': can_change_info,
            'can_invite_users': can_invite_users,
            'can_post_messages': can_post_messages,
            'can_edit_messages': can_edit_messages,
            'can_pin_messages': can_pin_messages,
            'can_manage_topics': can_manage_topics,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="promoteChatMember",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to promote/demote chat member {user_id} in chat {chat_id}. Error: {e}")
            raise
    def reopenForumTopic(
        self,
        chat_id: Union[int, str],
        message_thread_id: int,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to reopen a closed topic in a forum supergroup chat. The bot must be
        an administrator in the chat for this to work and must have the can_manage_topics
        administrator rights, unless it is the creator of the topic.

        Args:
            chat_id: Unique identifier for the target chat (supergroup username or ID).
            message_thread_id: Unique identifier for the target message thread of the forum topic.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If 'chat_id' or 'message_thread_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for reopenForumTopic.")
        if not isinstance(message_thread_id, int) or message_thread_id <= 0:
            raise ValueError("message_thread_id must be a positive integer for reopenForumTopic.")

        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="reopenForumTopic",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to reopen forum topic {message_thread_id} in chat {chat_id}. Error: {e}")
            raise

    
    def reopenGeneralForumTopic(
        self,
        chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to reopen a closed General forum topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have
        the can_manage_topics administrator rights.

        Args:
            chat_id: Unique identifier for the target chat (supergroup username or ID).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for reopenGeneralForumTopic.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="reopenGeneralForumTopic",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to reopen general forum topic in chat {chat_id}. Error: {e}")
            raise

 

    def restrictChatMember(
        self,
        chat_id: Union[int, str],
        user_id: int,
        permissions: Dict[str, bool],
        until_date: Optional[Union[int, str]] = None,
        use_independent_chat_permissions: Optional[bool] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to restrict a user in a supergroup or a channel.
        The bot must be an administrator in the chat for this to work and must have
        the can_restrict_members administrator right.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            user_id: Unique identifier of the target user.
            permissions: A JSON-serialized object for new user permissions.
            until_date: Date when the user's restrictions will be lifted. Unix time.
                        If user is restricted for more than 366 days or less than 30 seconds
                        from the current time, they are considered to be restricted forever.
            use_independent_chat_permissions: Pass True if chat permissions are set independently.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If 'chat_id', 'user_id', or 'permissions' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for restrictChatMember.")
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("user_id must be a positive integer for restrictChatMember.")
        if not isinstance(permissions, dict):
            raise ValueError("permissions must be a dictionary for restrictChatMember.")

        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            'permissions': permissions, # Will be JSON dumped
            'until_date': until_date,
            'use_independent_chat_permissions': use_independent_chat_permissions,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        # Serialize the permissions dictionary
        if 'permissions' in clean_payload:
            clean_payload['permissions'] = json.dumps(clean_payload['permissions'])

        try:
            return self.request(
                method="restrictChatMember",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to restrict chat member {user_id} in chat {chat_id}. Error: {e}")
            raise

 

    def revokeChatInviteLink(
        self,
        chat_id: Union[int, str],
        invite_link: str,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to revoke an invite link created by the bot.
        If the primary invite link is revoked, a new one is automatically generated.
        The bot must be an administrator in the chat for this to work and must have
        the can_invite_users administrator right.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel
                     (in the format @channelusername).
            invite_link: The invite link to revoke.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the revoked ChatInviteLink object.

        Raises:
            ValueError: If 'chat_id' or 'invite_link' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for revokeChatInviteLink.")
        if not invite_link:
            raise ValueError("invite_link is required for revokeChatInviteLink.")

        payload = {
            'chat_id': chat_id,
            'invite_link': invite_link,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="revokeChatInviteLink",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to revoke chat invite link {invite_link} for chat {chat_id}. Error: {e}")
            raise

 

    def sendAnimation(
        self,
        chat_id: Union[int, str],
        animation: Union[str, bytes],  # file_id, URL, or raw bytes
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = 'html',
        caption_entities: Optional[list[Dict[str, Any]]] = None,
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to send animation files (GIF, H.264/MPEG-4 AVC video without sound, etc.).
        Bots can currently send animations of up to 50 MB in size, this limit may be changed in the future.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            animation: Animation to send. Pass a file_id as string to send an animation
                       that exists on the Telegram servers, a HTTP URL as a string for Telegram to
                       get an animation from the Internet, or bytes to upload a new animation.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            caption: Animation caption (may also be used when resending animations by file_id), 0-1024 characters
                     after entities parsing.
            parse_mode: Mode for parsing entities in the animation caption.
            caption_entities: A JSON-serialized list of special entities that appear in the caption.
            has_spoiler: Pass True if the animation needs to be covered with a spoiler animation.
            disable_notification: Sends the message silently.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            reply_markup: A JSON-serialized object for an inline keyboard, custom reply keyboard, etc.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the sent Message.

        Raises:
            ValueError: If 'chat_id' or 'animation' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendAnimation.")
        if not animation:
            raise ValueError("animation is required for sendAnimation.")

        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'caption': caption,
            'parse_mode': parse_mode,
            'has_spoiler': has_spoiler,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            **kwargs
        }

        files = {}
        if isinstance(animation, bytes):
            files['animation'] = ('animation.gif', animation, 'image/gif') # Mime type can be more specific
        elif isinstance(animation, str) and (animation.startswith('http://') or animation.startswith('https://')):
            payload['animation'] = animation # Pass URL in payload
        else: # Assume it's a file_id
            payload['animation'] = animation

        # Serialize JSON-compatible values
        if isinstance(caption_entities, list):
            payload['caption_entities'] = json.dumps(caption_entities)
        if isinstance(reply_parameters, dict):
            payload['reply_parameters'] = json.dumps(reply_parameters)
        if isinstance(reply_markup, dict):
            payload['reply_markup'] = json.dumps(reply_markup)

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="sendAnimation",
                payload=clean_payload,
                return_response=return_response,
                files=files if files else None # Pass files only if present
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send animation to chat {chat_id}. Error: {e}")
            raise
        finally:
            # Ensure file handles are closed if opened (if animation was a file path)
            if 'animation' in files and hasattr(files['animation'][1], 'close'):
                files['animation'][1].close()


 

    def sendAudio(
        self,
        chat_id: Union[int, str],
        audio: Union[str, bytes], # file_id, URL, or raw bytes
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = 'html',
        caption_entities: Optional[list[Dict[str, Any]]] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        thumbnail: Optional[Union[str, bytes]] = None, # file_id, URL, or raw bytes
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to send audio files, if you want Telegram clients to display them in the music player.
        Your audio must be in .MP3 format. Bots can currently send audio files of up to 50 MB in size,
        this limit may be changed in the future.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            audio: Audio file to send. Pass a file_id as string to send an audio file
                   that exists on the Telegram servers, a HTTP URL as a string for Telegram to
                   get an audio file from the Internet, or bytes to upload a new audio file.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            caption: Audio caption, 0-1024 characters after entities parsing.
            parse_mode: Mode for parsing entities in the audio caption.
            caption_entities: A JSON-serialized list of special entities that appear in the caption.
            duration: Duration of the audio in seconds.
            performer: Performer of the audio.
            title: Title of the audio.
            thumbnail: Thumbnail of the file sent; can be a file_id, HTTP URL, or bytes.
            disable_notification: Sends the message silently.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            reply_markup: A JSON-serialized object for an inline keyboard, custom reply keyboard, etc.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the sent Message.

        Raises:
            ValueError: If 'chat_id' or 'audio' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendAudio.")
        if not audio:
            raise ValueError("audio is required for sendAudio.")

        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'caption': caption,
            'parse_mode': parse_mode,
            'duration': duration,
            'performer': performer,
            'title': title,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            **kwargs
        }

        files = {}
        if isinstance(audio, bytes):
            files['audio'] = ('audio.mp3', audio, 'audio/mpeg')
        elif isinstance(audio, str) and (audio.startswith('http://') or audio.startswith('https://')):
            payload['audio'] = audio
        else:
            payload['audio'] = audio

        if thumbnail:
            if isinstance(thumbnail, bytes):
                files['thumbnail'] = ('thumbnail.jpg', thumbnail, 'image/jpeg')
            elif isinstance(thumbnail, str) and (thumbnail.startswith('http://') or thumbnail.startswith('https://')):
                payload['thumbnail'] = thumbnail
            else:
                payload['thumbnail'] = thumbnail

        # Serialize JSON-compatible values
        if isinstance(caption_entities, list):
            payload['caption_entities'] = json.dumps(caption_entities)
        if isinstance(reply_parameters, dict):
            payload['reply_parameters'] = json.dumps(reply_parameters)
        if isinstance(reply_markup, dict):
            payload['reply_markup'] = json.dumps(reply_markup)

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="sendAudio",
                payload=clean_payload,
                return_response=return_response,
                files=files if files else None
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send audio to chat {chat_id}. Error: {e}")
            raise
        finally:
            # Close file handles if they were opened as bytes
            for f_key in ['audio', 'thumbnail']:
                if f_key in files and hasattr(files[f_key][1], 'close'):
                    files[f_key][1].close()


 

    def sendChatAction(
        self,
        chat_id: Union[int, str],
        action: str,
        message_thread_id: Optional[int] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method when you need to tell the user that something is happening on the bot's side.
        The status is set for 5 seconds or until the bot sends the next message,
        whichever comes first.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            action: Type of action to broadcast. Choose one, depending on what the user is about to receive:
                    'typing' for text messages, 'upload_photo' for photos, 'record_video' or 'upload_video'
                    for video files, 'record_voice' or 'upload_voice' for voice notes, 'upload_document'
                    for general files, 'choose_sticker' for stickers, 'find_location' for location data,
                    'record_video_note' or 'upload_video_note' for video notes.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If 'chat_id' or 'action' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendChatAction.")
        if not action or not isinstance(action, str):
            raise ValueError("action is required and must be a string for sendChatAction.")
        # Optional: Add validation for allowed 'action' values
        allowed_actions = [
            'typing', 'upload_photo', 'record_video', 'upload_video', 'record_voice',
            'upload_voice', 'upload_document', 'choose_sticker', 'find_location',
            'record_video_note', 'upload_video_note'
        ]
        if action not in allowed_actions:
            logging.warning(f"'{action}' is not a standard chat action. Proceeding, but verify API documentation.")

        payload = {
            'chat_id': chat_id,
            'action': action,
            'message_thread_id': message_thread_id,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="sendChatAction",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send chat action '{action}' to chat {chat_id}. Error: {e}")
            raise

 

    def sendContact(
        self,
        chat_id: Union[int, str],
        phone_number: str,
        first_name: str,
        message_thread_id: Optional[int] = None,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to send phone contacts.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            phone_number: Contact's phone number.
            first_name: Contact's first name.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            last_name: Contact's last name.
            vcard: Additional data about the contact in the form of a vCard.
            disable_notification: Sends the message silently.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            reply_markup: A JSON-serialized object for an inline keyboard, custom reply keyboard, etc.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the sent Message.

        Raises:
            ValueError: If 'chat_id', 'phone_number', or 'first_name' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendContact.")
        if not phone_number:
            raise ValueError("phone_number is required for sendContact.")
        if not first_name:
            raise ValueError("first_name is required for sendContact.")

        payload = {
            'chat_id': chat_id,
            'phone_number': phone_number,
            'first_name': first_name,
            'message_thread_id': message_thread_id,
            'last_name': last_name,
            'vcard': vcard,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            **kwargs
        }

        # Serialize JSON-compatible values
        if isinstance(reply_parameters, dict):
            payload['reply_parameters'] = json.dumps(reply_parameters)
        if isinstance(reply_markup, dict):
            payload['reply_markup'] = json.dumps(reply_markup)

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="sendContact",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send contact to chat {chat_id}. Error: {e}")
            raise

 

    def sendDice(
        self,
        chat_id: Union[int, str],
        message_thread_id: Optional[int] = None,
        emoji: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to send an animated emoji that will display a random value.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            emoji: Emoji on which the dice throw animation is based.
                   Currently, must be one of "🎲", "🎯", "🏀", "⚽", "🎳", or "🎰".
                   Defaults to "🎲".
            disable_notification: Sends the message silently.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            reply_markup: A JSON-serialized object for an inline keyboard, custom reply keyboard, etc.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the sent Message.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendDice.")
        
        allowed_emojis = ["🎲", "🎯", "🏀", "⚽", "🎳", "🎰"]
        if emoji is not None and emoji not in allowed_emojis:
            logging.warning(f"'{emoji}' is not a standard dice emoji. Proceeding, but verify API documentation.")

        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'emoji': emoji,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            **kwargs
        }

        # Serialize JSON-compatible values
        if isinstance(reply_parameters, dict):
            payload['reply_parameters'] = json.dumps(reply_parameters)
        if isinstance(reply_markup, dict):
            payload['reply_markup'] = json.dumps(reply_markup)

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="sendDice",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send dice to chat {chat_id}. Error: {e}")
            raise

 

    def sendDocument(
        self,
        chat_id: Union[int, str],
        document: Union[str, bytes], # file_id, URL, or raw bytes
        message_thread_id: Optional[int] = None,
        thumbnail: Optional[Union[str, bytes]] = None, # file_id, URL, or raw bytes
        caption: Optional[str] = None,
        parse_mode: Optional[str] = 'html',
        caption_entities: Optional[list[Dict[str, Any]]] = None,
        disable_content_type_detection: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to send general files. Bots can currently send files of up to 50 MB in size,
        this limit may be changed in the future.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            document: File to send. Pass a file_id as string to send a file that exists on
                      the Telegram servers, a HTTP URL as a string for Telegram to get a file
                      from the Internet, or bytes to upload a new file.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            thumbnail: Thumbnail of the file sent; can be a file_id, HTTP URL, or bytes.
            caption: Document caption (may also be used when resending documents by file_id),
                     0-1024 characters after entities parsing.
            parse_mode: Mode for parsing entities in the document caption.
            caption_entities: A JSON-serialized list of special entities that appear in the caption.
            disable_content_type_detection: Disables automatic server-side content type detection for files
                                            uploaded using multipart/form-data.
            disable_notification: Sends the message silently.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            reply_markup: A JSON-serialized object for an inline keyboard, custom reply keyboard, etc.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the sent Message.

        Raises:
            ValueError: If 'chat_id' or 'document' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendDocument.")
        if not document:
            raise ValueError("document is required for sendDocument.")

        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'caption': caption,
            'parse_mode': parse_mode,
            'disable_content_type_detection': disable_content_type_detection,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            **kwargs
        }

        files = {}
        if isinstance(document, bytes):
            files['document'] = ('document.bin', document, 'application/octet-stream') # Generic binary
        elif isinstance(document, str) and (document.startswith('http://') or document.startswith('https://')):
            payload['document'] = document
        else:
            payload['document'] = document

        if thumbnail:
            if isinstance(thumbnail, bytes):
                files['thumbnail'] = ('thumbnail.jpg', thumbnail, 'image/jpeg')
            elif isinstance(thumbnail, str) and (thumbnail.startswith('http://') or thumbnail.startswith('https://')):
                payload['thumbnail'] = thumbnail
            else:
                payload['thumbnail'] = thumbnail

        # Serialize JSON-compatible values
        if isinstance(caption_entities, list):
            payload['caption_entities'] = json.dumps(caption_entities)
        if isinstance(reply_parameters, dict):
            payload['reply_parameters'] = json.dumps(reply_parameters)
        if isinstance(reply_markup, dict):
            payload['reply_markup'] = json.dumps(reply_markup)

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="sendDocument",
                payload=clean_payload,
                return_response=return_response,
                files=files if files else None
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send document to chat {chat_id}. Error: {e}")
            raise
        finally:
            # Close file handles if they were opened as bytes
            for f_key in ['document', 'thumbnail']:
                if f_key in files and hasattr(files[f_key][1], 'close'):
                    files[f_key][1].close()

    def sendLocation(
        self,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        message_thread_id: Optional[int] = None,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to send point on the map.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            latitude: Latitude of the location.
            longitude: Longitude of the location.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            horizontal_accuracy: The radius of uncertainty for the location, in meters.
            live_period: Period in seconds for which the location will be updated.
                         (for live locations, should be between 60 and 86400).
            heading: For live locations, direction in which the user is moving, in degrees. 1-360.
                     Not applicable if live_period is not specified.
            proximity_alert_radius: For live locations, maximum distance for proximity alerts about approaching another chat member.
                                    2-100000. Not applicable if live_period is not specified.
            disable_notification: Sends the message silently.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            reply_markup: A JSON-serialized object for an inline keyboard, custom reply keyboard, etc.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the sent Message.

        Raises:
            ValueError: If 'chat_id', 'latitude', or 'longitude' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendLocation.")
        if not isinstance(latitude, (int, float)):
            raise ValueError("latitude must be a number for sendLocation.")
        if not isinstance(longitude, (int, float)):
            raise ValueError("longitude must be a number for sendLocation.")

        payload = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            'message_thread_id': message_thread_id,
            'horizontal_accuracy': horizontal_accuracy,
            'live_period': live_period,
            'heading': heading,
            'proximity_alert_radius': proximity_alert_radius,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            **kwargs
        }

        # Serialize JSON-compatible values
        if isinstance(reply_parameters, dict):
            payload['reply_parameters'] = json.dumps(reply_parameters)
        if isinstance(reply_markup, dict):
            payload['reply_markup'] = json.dumps(reply_markup)

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="sendLocation",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send location to chat {chat_id}. Error: {e}")
            raise

    
    def sendMediaGroup(
        self,
        chat_id: Union[int, str],
        media: List[Dict[str, Any]], # List of InputMediaPhoto, InputMediaVideo, InputMediaAudio, InputMediaDocument
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to send a group of photos, videos, documents or audios as an album.
        Documents and audios can be only grouped with other documents and audios in a media group.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            media: A JSON-serialized array describing messages to be sent, must include 2-10 items.
                   Each item must be an InputMediaPhoto, InputMediaVideo, InputMediaAudio, or InputMediaDocument.
                   For file uploads, specify "attach://<file_name_in_files_dict>" for 'media' field in InputMedia.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            disable_notification: Sends the message silently. Users will receive a notification with no sound.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, an array of the sent Messages is returned.

        Raises:
            ValueError: If 'chat_id' or 'media' is missing or invalid, or if media list size is not 2-10.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendMediaGroup.")
        if not isinstance(media, list) or not (2 <= len(media) <= 10):
            raise ValueError("media must be a list with 2-10 items for sendMediaGroup.")

        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            **kwargs
        }

        files = {}
        # Iterate through media to handle file uploads
        for i, item in enumerate(media):
            if 'media' in item and isinstance(item['media'], bytes):
                file_name = f"attached_file_{i}"
                files[file_name] = (f"file_{i}.bin", item['media'], 'application/octet-stream')
                item['media'] = f"attach://{file_name}" # Update the media path to point to the attachment

            if 'thumbnail' in item and isinstance(item['thumbnail'], bytes):
                thumb_name = f"attached_thumb_{i}"
                files[thumb_name] = (f"thumb_{i}.jpg", item['thumbnail'], 'image/jpeg')
                item['thumbnail'] = f"attach://{thumb_name}"

            # Ensure caption_entities are JSON dumped within each media item if present
            if 'caption_entities' in item and isinstance(item['caption_entities'], list):
                item['caption_entities'] = json.dumps(item['caption_entities'])

        payload['media'] = json.dumps(media) # Serialize the entire media array

        # Serialize JSON-compatible values
        if isinstance(reply_parameters, dict):
            payload['reply_parameters'] = json.dumps(reply_parameters)

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="sendMediaGroup",
                payload=clean_payload,
                return_response=return_response,
                files=files if files else None
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send media group to chat {chat_id}. Error: {e}")
            raise
        finally:
            # Close file handles if they were opened as bytes
            for f_data in files.values():
                if hasattr(f_data[1], 'close'):
                    f_data[1].close()

    def sendPhoto(
        self,
        chat_id: Union[int, str],
        photo: Union[str, bytes],  # file_id, URL, or raw bytes
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = 'html',
        caption_entities: Optional[list[Dict[str, Any]]] = None,
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to send photos.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            photo: Photo to send. Pass a file_id as string to send a photo that exists on the Telegram servers,
                   a HTTP URL as a string for Telegram to get a photo from the Internet, or bytes to upload a new photo.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            caption: Photo caption (may also be used when resending photos by file_id), 0-1024 characters
                     after entities parsing.
            parse_mode: Mode for parsing entities in the photo caption.
            caption_entities: A JSON-serialized list of special entities that appear in the caption.
            has_spoiler: Pass True if the photo needs to be covered with a spoiler animation.
            disable_notification: Sends the message silently.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            reply_markup: A JSON-serialized object for an inline keyboard, custom reply keyboard, etc.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the sent Message.

        Raises:
            ValueError: If 'chat_id' or 'photo' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendPhoto.")
        if not photo:
            raise ValueError("photo is required for sendPhoto.")

        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'caption': caption,
            'parse_mode': parse_mode,
            'has_spoiler': has_spoiler,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            'reply_markup': reply_markup,
            **kwargs
        }
        clean_payload = self._prepare_payload(payload)
        
        # if isinstance(photo, bytes):
        #     files['photo'] = ('photo.jpg', photo, 'image/jpeg')
        # elif isinstance(photo, str) and (photo.startswith('http://') or photo.startswith('https://')):
        #     payload['photo'] = photo
        # else: # Assume it's a file_id
        #     payload['photo'] = photo

        # # Serialize JSON-compatible values
        # if isinstance(caption_entities, list):
        #     payload['caption_entities'] = json.dumps(caption_entities)
        # if isinstance(reply_parameters, dict):
        #     payload['reply_parameters'] = json.dumps(reply_parameters)
        
        if isinstance(clean_payload.get('reply_markup'), dict):
            clean_payload['reply_markup'] = json.dumps(clean_payload['reply_markup'])

        # # Remove None values from the payload
        # clean_payload = {k: v for k, v in payload.items() if v is not None}
        
        photo = InputFile(photo)
        # print("photo is an InputFile object")
        file = open(photo.file_path, 'rb')
        file = {"photo": file}
        try:
            result = self.request(
                method="sendPhoto",
                payload=clean_payload,
                return_response=return_response,
                files=file if file else None
            )
            return Message(**result)

        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send photo to chat {chat_id}. Error: {e}")
            raise
        # finally:
        #     if 'photo' in files and hasattr(files['photo'][1], 'close'):
        #         files['photo'][1].close()

    def sendPoll(
        self,
        chat_id: Union[int, str],
        question: str,
        options: List[str],
        message_thread_id: Optional[int] = None,
        is_anonymous: Optional[bool] = None,
        type: Optional[str] = None, # 'quiz' or 'regular'
        allows_multiple_answers: Optional[bool] = None,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_parse_mode: Optional[str] = 'html',
        explanation_entities: Optional[list[Dict[str, Any]]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None, # Unix timestamp
        is_closed: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to send a native poll.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            question: Poll question, 1-300 characters.
            options: A list of answer options, 2-10 strings 1-100 characters each.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            is_anonymous: True, if the poll needs to be anonymous, defaults to True.
            type: Poll type, 'quiz' or 'regular', defaults to 'regular'.
            allows_multiple_answers: True, if the poll allows multiple answers, ignored for polls in quiz mode.
            correct_option_id: 0-based identifier of the correct answer option, required for polls in quiz mode.
            explanation: Text that is shown when a user chooses an incorrect answer or taps on the lamp icon
                         in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing.
            explanation_parse_mode: Mode for parsing entities in the explanation.
            explanation_entities: A JSON-serialized list of special entities that appear in the poll explanation.
            open_period: Amount of time in seconds the poll will be active after creation, 5-600.
            close_date: Point in time (Unix timestamp) when the poll will be automatically closed.
                        Must be at least 5 and no more than 600 seconds in the future.
            is_closed: Pass True, if the poll needs to be immediately closed.
            disable_notification: Sends the message silently.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            reply_markup: A JSON-serialized object for an inline keyboard, custom reply keyboard, etc.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the sent Message.

        Raises:
            ValueError: If 'chat_id', 'question', or 'options' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendPoll.")
        if not question:
            raise ValueError("question is required for sendPoll.")
        if not isinstance(options, list) or not (2 <= len(options) <= 10):
            raise ValueError("options must be a list with 2-10 strings for sendPoll.")

        payload = {
            'chat_id': chat_id,
            'question': question,
            'options': json.dumps(options), # Must be JSON-serialized
            'message_thread_id': message_thread_id,
            'is_anonymous': is_anonymous,
            'type': type,
            'allows_multiple_answers': allows_multiple_answers,
            'correct_option_id': correct_option_id,
            'explanation': explanation,
            'explanation_parse_mode': explanation_parse_mode,
            'open_period': open_period,
            'close_date': close_date,
            'is_closed': is_closed,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            **kwargs
        }

        # Serialize JSON-compatible values
        if isinstance(explanation_entities, list):
            payload['explanation_entities'] = json.dumps(explanation_entities)
        if isinstance(reply_parameters, dict):
            payload['reply_parameters'] = json.dumps(reply_parameters)
        if isinstance(reply_markup, dict):
            payload['reply_markup'] = json.dumps(reply_markup)

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="sendPoll",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send poll to chat {chat_id}. Error: {e}")
            raise

    def sendVenue(
        self,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        message_thread_id: Optional[int] = None,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to send information about a venue.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            latitude: Latitude of the venue.
            longitude: Longitude of the venue.
            title: Name of the venue.
            address: Address of the venue.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            foursquare_id: Foursquare identifier of the venue.
            foursquare_type: Foursquare type of the venue.
            google_place_id: Google Places identifier of the venue.
            google_place_type: Google Places type of the venue.
            disable_notification: Sends the message silently.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            reply_markup: A JSON-serialized object for an inline keyboard, custom reply keyboard, etc.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the sent Message.

        Raises:
            ValueError: If 'chat_id', 'latitude', 'longitude', 'title', or 'address' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendVenue.")
        if not isinstance(latitude, (int, float)):
            raise ValueError("latitude must be a number for sendVenue.")
        if not isinstance(longitude, (int, float)):
            raise ValueError("longitude must be a number for sendVenue.")
        if not title:
            raise ValueError("title is required for sendVenue.")
        if not address:
            raise ValueError("address is required for sendVenue.")

        payload = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            'title': title,
            'address': address,
            'message_thread_id': message_thread_id,
            'foursquare_id': foursquare_id,
            'foursquare_type': foursquare_type,
            'google_place_id': google_place_id,
            'google_place_type': google_place_type,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            **kwargs
        }

        # Serialize JSON-compatible values
        if isinstance(reply_parameters, dict):
            payload['reply_parameters'] = json.dumps(reply_parameters)
        if isinstance(reply_markup, dict):
            payload['reply_markup'] = json.dumps(reply_markup)

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="sendVenue",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send venue to chat {chat_id}. Error: {e}")
            raise

    def sendVideo(
        self,
        chat_id: Union[int, str],
        video: Union[str, bytes], # file_id, URL, or raw bytes
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumbnail: Optional[Union[str, bytes]] = None, # file_id, URL, or raw bytes
        caption: Optional[str] = None,
        parse_mode: Optional[str] = 'html',
        caption_entities: Optional[list[Dict[str, Any]]] = None,
        has_spoiler: Optional[bool] = None,
        supports_streaming: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document).
        Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            video: Video to send. Pass a file_id as string to send a video that exists on the Telegram servers,
                   a HTTP URL as a string for Telegram to get a video from the Internet, or bytes to upload a new video.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            duration: Duration of sent video in seconds.
            width: Video width.
            height: Video height.
            thumbnail: Thumbnail of the file sent; can be a file_id, HTTP URL, or bytes.
            caption: Video caption (may also be used when resending videos by file_id), 0-1024 characters
                     after entities parsing.
            parse_mode: Mode for parsing entities in the video caption.
            caption_entities: A JSON-serialized list of special entities that appear in the caption.
            has_spoiler: Pass True if the video needs to be covered with a spoiler animation.
            supports_streaming: Pass True if the uploaded video is suitable for streaming.
            disable_notification: Sends the message silently.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            reply_markup: A JSON-serialized object for an inline keyboard, custom reply keyboard, etc.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the sent Message.

        Raises:
            ValueError: If 'chat_id' or 'video' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendVideo.")
        if not video:
            raise ValueError("video is required for sendVideo.")

        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'duration': duration,
            'width': width,
            'height': height,
            'caption': caption,
            'parse_mode': parse_mode,
            'has_spoiler': has_spoiler,
            'supports_streaming': supports_streaming,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            **kwargs
        }
        clean_payload = self._prepare_payload(payload)
        if isinstance(clean_payload.get('reply_markup'), dict):
            clean_payload['reply_markup'] = json.dumps(clean_payload['reply_markup'])

        video = InputFile(video)
        file = open(video.file_path, 'rb')
        files = {"video": file}
        # files = {}
        # if isinstance(video, bytes):
        #     files['video'] = ('video.mp4', video, 'video/mp4')
        # elif isinstance(video, str) and (video.startswith('http://') or video.startswith('https://')):
        #     payload['video'] = video
        # else:
        #     payload['video'] = video

        # if thumbnail:
        #     if isinstance(thumbnail, bytes):
        #         files['thumbnail'] = ('thumbnail.jpg', thumbnail, 'image/jpeg')
        #     elif isinstance(thumbnail, str) and (thumbnail.startswith('http://') or thumbnail.startswith('https://')):
        #         payload['thumbnail'] = thumbnail
        #     else:
        #         payload['thumbnail'] = thumbnail

        # # Serialize JSON-compatible values
        # if isinstance(caption_entities, list):
        #     payload['caption_entities'] = json.dumps(caption_entities)
        # if isinstance(reply_parameters, dict):
        #     payload['reply_parameters'] = json.dumps(reply_parameters)
        # if isinstance(reply_markup, dict):
        #     payload['reply_markup'] = json.dumps(reply_markup)

        # # Remove None values from the payload
        # clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            result = self.request(
                method="sendVideo",
                payload=clean_payload,
                return_response=return_response,
                files=files if files else None
            )
            # print(result)
            return Message(**result)
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send video to chat {chat_id}. Error: {e}")
            raise
        finally:
            for f_key in ['video', 'thumbnail']:
                if f_key in files and hasattr(files[f_key][1], 'close'):
                    files[f_key][1].close()

    def sendVideoNote(
        self,
        chat_id: Union[int, str],
        video_note: Union[str, bytes], # file_id or raw bytes
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        length: Optional[int] = None, # Video width and height (diameter)
        thumbnail: Optional[Union[str, bytes]] = None, # file_id or raw bytes
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to send video messages. Telegram clients support rounded square mp4 videos
        of up to 1 minute long.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            video_note: Video note to send. Pass a file_id as string to send a video note that exists on
                        the Telegram servers, or bytes to upload a new video note. Sending video notes
                        by a URL is currently unsupported.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            duration: Duration of sent video in seconds.
            length: Video width and height, i.e. diameter of the video message, in pixels.
            thumbnail: Thumbnail of the file sent; can be a file_id or bytes.
            disable_notification: Sends the message silently.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            reply_markup: A JSON-serialized object for an inline keyboard, custom reply keyboard, etc.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the sent Message.

        Raises:
            ValueError: If 'chat_id' or 'video_note' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendVideoNote.")
        if not video_note:
            raise ValueError("video_note is required for sendVideoNote.")
        
        if isinstance(video_note, str) and (video_note.startswith('http://') or video_note.startswith('https://')):
            logging.warning("Sending video notes by URL is generally unsupported by Telegram Bot API. It's recommended to upload as bytes or use a file_id.")


        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'duration': duration,
            'length': length,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            **kwargs
        }

        files = {}
        if isinstance(video_note, bytes):
            files['video_note'] = ('video_note.mp4', video_note, 'video/mp4')
        else: # Assume it's a file_id or a URL (though URLs are warned against)
            payload['video_note'] = video_note

        if thumbnail:
            if isinstance(thumbnail, bytes):
                files['thumbnail'] = ('thumbnail.jpg', thumbnail, 'image/jpeg')
            elif isinstance(thumbnail, str) and (thumbnail.startswith('http://') or thumbnail.startswith('https://')):
                payload['thumbnail'] = thumbnail
            else:
                payload['thumbnail'] = thumbnail

        # Serialize JSON-compatible values
        if isinstance(reply_parameters, dict):
            payload['reply_parameters'] = json.dumps(reply_parameters)
        if isinstance(reply_markup, dict):
            payload['reply_markup'] = json.dumps(reply_markup)

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="sendVideoNote",
                payload=clean_payload,
                return_response=return_response,
                files=files if files else None
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send video note to chat {chat_id}. Error: {e}")
            raise
        finally:
            for f_key in ['video_note', 'thumbnail']:
                if f_key in files and hasattr(files[f_key][1], 'close'):
                    files[f_key][1].close()

    def sendVoice(
        self,
        chat_id: Union[int, str],
        voice: Union[str, bytes], # file_id, URL, or raw bytes
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = 'html',
        caption_entities: Optional[list[Dict[str, Any]]] = None,
        duration: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_parameters: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to send audio files, if you want Telegram clients to display the file as a
        playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS
        (other formats may be sent as Audio or Document).

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            voice: Audio file to send. Pass a file_id as string to send an audio file that exists on
                   the Telegram servers, a HTTP URL as a string for Telegram to get an audio file
                   from the Internet, or bytes to upload a new audio file.
            message_thread_id: Unique identifier for the target message thread (for forum supergroups).
            caption: Voice message caption, 0-1024 characters after entities parsing.
            parse_mode: Mode for parsing entities in the voice message caption.
            caption_entities: A JSON-serialized list of special entities that appear in the caption.
            duration: Duration of the voice message in seconds.
            disable_notification: Sends the message silently.
            protect_content: Protects the contents of the sent message from forwarding and saving.
            reply_parameters: Description of the message to reply to.
            reply_markup: A JSON-serialized object for an inline keyboard, custom reply keyboard, etc.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.
            On success, returns the sent Message.

        Raises:
            ValueError: If 'chat_id' or 'voice' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for sendVoice.")
        if not voice:
            raise ValueError("voice is required for sendVoice.")

        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            'caption': caption,
            'parse_mode': parse_mode,
            'duration': duration,
            'disable_notification': disable_notification,
            'protect_content': protect_content,
            **kwargs
        }

        files = {}
        if isinstance(voice, bytes):
            files['voice'] = ('voice.ogg', voice, 'audio/ogg') # OGG/OPUS is standard for voice notes
        elif isinstance(voice, str) and (voice.startswith('http://') or voice.startswith('https://')):
            payload['voice'] = voice
        else:
            payload['voice'] = voice

        # Serialize JSON-compatible values
        if isinstance(caption_entities, list):
            payload['caption_entities'] = json.dumps(caption_entities)
        if isinstance(reply_parameters, dict):
            payload['reply_parameters'] = json.dumps(reply_parameters)
        if isinstance(reply_markup, dict):
            payload['reply_markup'] = json.dumps(reply_markup)

        # Remove None values from the payload
        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="sendVoice",
                payload=clean_payload,
                return_response=return_response,
                files=files if files else None
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send voice to chat {chat_id}. Error: {e}")
            raise
        finally:
            if 'voice' in files and hasattr(files['voice'][1], 'close'):
                files['voice'][1].close()

    def setChatAdministratorCustomTitle(
        self,
        chat_id: Union[int, str],
        user_id: int,
        custom_title: str,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to set a custom title for an administrator in a supergroup promoted by the bot.
        Returns True on success.

        Args:
            chat_id: Unique identifier for the target chat or username of the target supergroup.
            user_id: Unique identifier of the target user.
            custom_title: New custom title for the administrator; 0-16 characters, emoji are not allowed.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If 'chat_id', 'user_id', or 'custom_title' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for setChatAdministratorCustomTitle.")
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("user_id must be a positive integer for setChatAdministratorCustomTitle.")
        if not isinstance(custom_title, str) or len(custom_title) > 16:
            raise ValueError("custom_title is required and must be a string up to 16 characters for setChatAdministratorCustomTitle.")

        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            'custom_title': custom_title,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="setChatAdministratorCustomTitle",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set custom title for admin {user_id} in chat {chat_id}. Error: {e}")
            raise

    def setChatDescription(
        self,
        chat_id: Union[int, str],
        description: Optional[str] = None, # Can be an empty string to clear
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to change the description of a group, a supergroup or a channel.
        The bot must be an administrator in the chat for this to work and must have the
        can_change_info administrator right.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            description: New chat description, 0-255 characters. Pass an empty string to clear the description.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for setChatDescription.")
        if description is not None and not isinstance(description, str):
            raise ValueError("description must be a string or None for setChatDescription.")
        if description is not None and len(description) > 255:
            logging.warning("Chat description exceeds 255 characters. It might be truncated by Telegram.")

        payload = {
            'chat_id': chat_id,
            'description': description,
            **kwargs
        }

        # Note: If description is an empty string, we want to keep it in the payload.
        # Only remove if it's explicitly None.
        clean_payload = {k: v for k, v in payload.items() if v is not None}
        # If description was explicitly passed as an empty string, ensure it's in clean_payload.
        if 'description' not in clean_payload and description == "":
            clean_payload['description'] = ""


        try:
            return self.request(
                method="setChatDescription",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set chat description for chat {chat_id}. Error: {e}")
            raise
    
    def setChatMenuButton(
        self,
        chat_id: Optional[Union[int, str]] = None,
        menu_button: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to change the bot's menu button in a private chat, or the default menu button.

        Args:
            chat_id: Unique identifier for the target private chat. If not specified,
                     the default bot's menu button will be changed for all private chats.
            menu_button: A JSON-serialized object for the bot's new menu button.
                         Defaults to MenuButtonDefault.
                         Can be:
                         - {'type': 'commands'}
                         - {'type': 'web_app', 'text': 'WebApp Name', 'web_app': {'url': 'https://example.com'}}
                         - {'type': 'default'}
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            requests.exceptions.RequestException: For request-related errors.
        """
        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        if menu_button:
            payload['menu_button'] = json.dumps(menu_button)

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="setChatMenuButton",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set chat menu button for chat {chat_id}. Error: {e}")
            raise

    def setChatPermissions(
        self,
        chat_id: Union[int, str],
        permissions: Dict[str, bool],
        use_independent_chat_permissions: Optional[bool] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to set default chat permissions for all members.
        The bot must be an administrator in the group or a supergroup for this to work and
        must have the can_restrict_members administrator rights.

        Args:
            chat_id: Unique identifier for the target chat or username of the target supergroup.
            permissions: A JSON-serialized object for new default chat permissions.
                         Example: {'can_send_messages': True, 'can_send_audios': False}
            use_independent_chat_permissions: Pass True if chat permissions are set independently
                                                of each other.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'chat_id' or 'permissions' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for setChatPermissions.")
        if not isinstance(permissions, dict):
            raise ValueError("permissions must be a dictionary for setChatPermissions.")

        payload = {
            'chat_id': chat_id,
            'permissions': json.dumps(permissions), # Must be JSON-serialized
            'use_independent_chat_permissions': use_independent_chat_permissions,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="setChatPermissions",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set chat permissions for chat {chat_id}. Error: {e}")
            raise

    def setChatPhoto(
        self,
        chat_id: Union[int, str],
        photo: Union[str, bytes], # File to upload as the new chat photo
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to set a new profile photo for the chat.
        The bot must be an administrator in the chat for this to work and must have
        the can_change_info administrator right.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            photo: New chat photo. A file_id of an existing file or raw bytes to upload.
                   Pass an empty string or None to delete the existing chat photo (this requires deleteChatPhoto method).
                   Note: The Telegram Bot API documentation usually implies a separate method for deleting.
                   For setting, it expects an InputFile or file_id.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'chat_id' or 'photo' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for setChatPhoto.")
        if not photo:
            # For deletion, use deleteChatPhoto. For setting, a photo is required.
            raise ValueError("photo (file_id or bytes) is required for setChatPhoto.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }
        files = {}

        if isinstance(photo, bytes):
            files['photo'] = ('chat_photo.jpg', photo, 'image/jpeg')
        elif isinstance(photo, str):
            payload['photo'] = photo # Assume it's a file_id or URL, though API often expects file_id here
        else:
            raise ValueError("photo must be bytes (for upload) or a string (for file_id).")

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="setChatPhoto",
                payload=clean_payload,
                return_response=return_response,
                files=files if files else None
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set chat photo for chat {chat_id}. Error: {e}")
            raise
        finally:
            if 'photo' in files and hasattr(files['photo'][1], 'close'):
                files['photo'][1].close()

    def setChatStickerSet(
        self,
        chat_id: Union[int, str],
        sticker_set_name: str,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to set a new group sticker set for a supergroup.
        The bot must be an administrator in the chat for this to work and must have
        the can_send_messages administrator right.

        Args:
            chat_id: Unique identifier for the target chat or username of the target supergroup.
            sticker_set_name: Name of the sticker set to be set as the group sticker set.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'chat_id' or 'sticker_set_name' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for setChatStickerSet.")
        if not sticker_set_name:
            raise ValueError("sticker_set_name is required for setChatStickerSet.")

        payload = {
            'chat_id': chat_id,
            'sticker_set_name': sticker_set_name,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="setChatStickerSet",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set chat sticker set for chat {chat_id}. Error: {e}")
            raise

    def setChatTitle(
        self,
        chat_id: Union[int, str],
        title: str,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to change the title of a chat. Titles can't be changed for private chats.
        The bot must be an administrator in the chat for this to work and must have
        the can_change_info administrator right.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            title: New chat title, 1-255 characters.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'chat_id' or 'title' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for setChatTitle.")
        if not title or not isinstance(title, str) or not (1 <= len(title) <= 255):
            raise ValueError("title is required and must be a string 1-255 characters for setChatTitle.")

        payload = {
            'chat_id': chat_id,
            'title': title,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="setChatTitle",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set chat title for chat {chat_id}. Error: {e}")
            raise

    def setMyCommands(
        self,
        commands: List[Dict[str, str]], # List of BotCommand objects
        scope: Optional[Dict[str, Any]] = None, # BotCommandScope object
        language_code: Optional[str] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to change the list of the bot's commands.
        See this manual for more details about bot commands: https://core.telegram.org/bots/features#commands

        Args:
            commands: A JSON-serialized list of bot commands to be set as the list of the bot's commands.
                      Example: [{'command': 'start', 'description': 'Start the bot'}, {'command': 'help', 'description': 'Get help'}]
            scope: A JSON-serialized object, describing scope of users for which the commands are relevant.
                   Defaults to BotCommandScopeDefault.
                   Example: {'type': 'all_private_chats'}
            language_code: A two-letter ISO 639-1 language code. If empty, commands will be applied
                           to all users, or to the users in the given scope for the default language.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'commands' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not isinstance(commands, list) or not all(isinstance(cmd, dict) and 'command' in cmd and 'description' in cmd for cmd in commands):
            raise ValueError("commands must be a list of dictionaries with 'command' and 'description' for setMyCommands.")

        payload = {
            'commands': json.dumps(commands), # Must be JSON-serialized
            'language_code': language_code,
            **kwargs
        }

        if scope:
            payload['scope'] = json.dumps(scope) # Must be JSON-serialized

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="setMyCommands",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set my commands. Error: {e}")
            raise

    def setMyDefaultAdministratorRights(
        self,
        rights: Optional[Dict[str, Any]] = None, # ChatAdministratorRights object
        for_channels: Optional[bool] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to change the default administrator rights requested by the bot when it's
        added as an administrator to groups or channels. These rights will be suggested to users,
        but they are free to modify the list before adding the bot. Returns True on success.

        Args:
            rights: A JSON-serialized object describing new default administrator rights.
                    If not specified, the default administrator rights will be cleared.
                    Example: {'can_manage_chat': True, 'can_delete_messages': True}
            for_channels: Pass True to change the default administrator rights of the bot in channels.
                          Otherwise, the default administrator rights of the bot for groups and supergroups will be changed.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'rights' is provided but not a dictionary.
            requests.exceptions.RequestException: For request-related errors.
        """
        payload = {
            'for_channels': for_channels,
            **kwargs
        }

        if rights is not None:
            if not isinstance(rights, dict):
                raise ValueError("rights must be a dictionary or None for setMyDefaultAdministratorRights.")
            payload['rights'] = json.dumps(rights) # Must be JSON-serialized

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="setMyDefaultAdministratorRights",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set my default administrator rights. Error: {e}")
            raise

    def setMyDescription(
        self,
        description: Optional[str] = None, # 0-512 characters
        language_code: Optional[str] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to change the bot's description, which is shown in the chat with the bot
        in the Bots, and Bot's profile pages.

        Args:
            description: New bot description; 0-512 characters. Pass an empty string to remove the
                         dedicated description for the given language.
            language_code: A two-letter ISO 639-1 language code. If empty, the description will be
                           applied to all users for the default language.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'description' is provided but not a string.
            requests.exceptions.RequestException: For request-related errors.
        """
        if description is not None and not isinstance(description, str):
            raise ValueError("description must be a string or None for setMyDescription.")
        if description is not None and len(description) > 512:
            logging.warning("Bot description exceeds 512 characters. It might be truncated by Telegram.")

        payload = {
            'description': description,
            'language_code': language_code,
            **kwargs
        }

        # Handle empty string for description explicitly, keep it if it's passed
        clean_payload = {k: v for k, v in payload.items() if v is not None}
        if 'description' not in clean_payload and description == "":
            clean_payload['description'] = ""

        try:
            return self.request(
                method="setMyDescription",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set my description. Error: {e}")
            raise

    
    def setMyName(
        self,
        name: Optional[str] = None, # 1-64 characters
        language_code: Optional[str] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to change the bot's name.

        Args:
            name: New bot name; 1-64 characters. Pass an empty string to remove the
                  dedicated name for the given language.
            language_code: A two-letter ISO 639-1 language code. If empty, the name will be
                           applied to all users for the default language.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'name' is provided but not a string or exceeds length.
            requests.exceptions.RequestException: For request-related errors.
        """
        if name is not None and not isinstance(name, str):
            raise ValueError("name must be a string or None for setMyName.")
        if name is not None and not (1 <= len(name) <= 64) and name != "":
            raise ValueError("name must be 1-64 characters or an empty string to clear for setMyName.")

        payload = {
            'name': name,
            'language_code': language_code,
            **kwargs
        }

        # Handle empty string for name explicitly, keep it if it's passed
        clean_payload = {k: v for k, v in payload.items() if v is not None}
        if 'name' not in clean_payload and name == "":
            clean_payload['name'] = ""

        try:
            return self.request(
                method="setMyName",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set my name. Error: {e}")
            raise

    def setMyShortDescription(
        self,
        short_description: Optional[str] = None, # 0-120 characters
        language_code: Optional[str] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to change the bot's short description, which is shown on the bot's profile page
        and is sent together with the link to the bot if users share it.

        Args:
            short_description: New bot short description; 0-120 characters. Pass an empty string to remove the
                               dedicated short description for the given language.
            language_code: A two-letter ISO 639-1 language code. If empty, the short description will be
                           applied to all users for the default language.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'short_description' is provided but not a string or exceeds length.
            requests.exceptions.RequestException: For request-related errors.
        """
        if short_description is not None and not isinstance(short_description, str):
            raise ValueError("short_description must be a string or None for setMyShortDescription.")
        if short_description is not None and len(short_description) > 120:
            logging.warning("Bot short description exceeds 120 characters. It might be truncated by Telegram.")

        payload = {
            'short_description': short_description,
            'language_code': language_code,
            **kwargs
        }

        # Handle empty string for short_description explicitly, keep it if it's passed
        clean_payload = {k: v for k, v in payload.items() if v is not None}
        if 'short_description' not in clean_payload and short_description == "":
            clean_payload['short_description'] = ""

        try:
            return self.request(
                method="setMyShortDescription",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to set my short description. Error: {e}")
            raise

    def unbanChatMember(
        self,
        chat_id: Union[int, str],
        user_id: int,
        only_if_banned: Optional[bool] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to unban a previously banned user in a supergroup or channel.
        The user will not return to the group or channel automatically, but will be able
        to join it via link, etc. The bot must be an administrator in the chat for this
        to work. By default, this method might also be used to automatically unban users
        if the chat is a supergroup and the user is banned for less than 24 hours.
        Returns True on success.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            user_id: Unique identifier of the target user.
            only_if_banned: Do nothing if the user is not banned (instead of throwing an error).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If 'chat_id' or 'user_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for unbanChatMember.")
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("user_id must be a positive integer for unbanChatMember.")

        payload = {
            'chat_id': chat_id,
            'user_id': user_id,
            'only_if_banned': only_if_banned,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="unbanChatMember",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to unban chat member {user_id} in chat {chat_id}. Error: {e}")
            raise

    def unbanChatSenderChat(
        self,
        chat_id: Union[int, str],
        sender_chat_id: int,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to unban a previously banned channel chat in a supergroup or channel.
        The bot must be an administrator in the chat for this to work and must have the
        can_restrict_members administrator right.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            sender_chat_id: Unique identifier of the previously banned sender chat.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'chat_id' or 'sender_chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for unbanChatSenderChat.")
        if not isinstance(sender_chat_id, int) or sender_chat_id <= 0:
            raise ValueError("sender_chat_id must be a positive integer for unbanChatSenderChat.")

        payload = {
            'chat_id': chat_id,
            'sender_chat_id': sender_chat_id,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="unbanChatSenderChat",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to unban chat sender chat {sender_chat_id} in chat {chat_id}. Error: {e}")
            raise

    def unhideGeneralForumTopic(
        self,
        chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to unhide the General forum topic in a forum supergroup chat.
        The bot must be an administrator in the chat for this to work and must have
        the can_manage_topics administrator rights.

        Args:
            chat_id: Unique identifier for the target chat (supergroup username or ID).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for unhideGeneralForumTopic.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="unhideGeneralForumTopic",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to unhide general forum topic in chat {chat_id}. Error: {e}")
            raise

    def unpinAllChatMessages(
        self,
        chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to clear the list of pinned messages in a chat.
        If the chat is not a private chat, the bot must be an administrator in the chat
        for this to work and must have the 'can_pin_messages' administrator right
        in the supergroup or channel.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for unpinAllChatMessages.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="unpinAllChatMessages",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to unpin all chat messages in chat {chat_id}. Error: {e}")
            raise

    def unpinAllForumTopicMessages(
        self,
        chat_id: Union[int, str],
        message_thread_id: int,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to clear the list of pinned messages in a forum topic.
        The bot must be an administrator in the chat for this to work and must have
        the can_pin_messages administrator right in the supergroup.

        Args:
            chat_id: Unique identifier for the target chat (supergroup username or ID).
            message_thread_id: Unique identifier for the target message thread of the forum topic.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'chat_id' or 'message_thread_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for unpinAllForumTopicMessages.")
        if not isinstance(message_thread_id, int) or message_thread_id <= 0:
            raise ValueError("message_thread_id must be a positive integer for unpinAllForumTopicMessages.")

        payload = {
            'chat_id': chat_id,
            'message_thread_id': message_thread_id,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="unpinAllForumTopicMessages",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to unpin all forum topic messages in chat {chat_id}, topic {message_thread_id}. Error: {e}")
            raise

    def unpinAllGeneralForumTopicMessages(
        self,
        chat_id: Union[int, str],
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to clear the list of pinned messages in the General forum topic.
        The bot must be an administrator in the chat for this to work and must have
        the can_pin_messages administrator right in the supergroup.

        Args:
            chat_id: Unique identifier for the target chat (supergroup username or ID).
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for unpinAllGeneralForumTopicMessages.")

        payload = {
            'chat_id': chat_id,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="unpinAllGeneralForumTopicMessages",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to unpin all general forum topic messages in chat {chat_id}. Error: {e}")
            raise

    def unpinChatMessage(
        self,
        chat_id: Union[int, str],
        message_id: Optional[int] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Use this method to remove a message from the list of pinned messages in a chat.
        If no message_id is specified, the most recently pinned message (by the bot) is unpinned.
        The bot must be an administrator in the chat for this to work and must have the
        can_pin_messages administrator right in the supergroup or channel.

        Args:
            chat_id: Unique identifier for the target chat or username of the target channel.
            message_id: Identifier of a message to unpin. If empty, the most recent pinned message (by the bot) is unpinned.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters for future extensions.

        Returns:
            requests.Response if return_response=True, None otherwise.
            Returns True on success.

        Raises:
            ValueError: If 'chat_id' is missing or invalid.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required for unpinChatMessage.")
        if message_id is not None and (not isinstance(message_id, int) or message_id <= 0):
            raise ValueError("message_id must be a positive integer or None for unpinChatMessage.")

        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="unpinChatMessage",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to unpin chat message {message_id if message_id else 'latest'} in chat {chat_id}. Error: {e}")
            raise
    

    def deleteMessage(
        self,
        chat_id: Union[int, str],
        message_id: int,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Delete a message.

        Args:
            chat_id: Unique identifier for the target chat.
            message_id: Identifier of the message to delete.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If required parameters are missing.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required.")
        if not message_id:
            raise ValueError("message_id is required.")

        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        try:
            return self.request(
                method="deleteMessage",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to delete message {message_id} in chat {chat_id}. Error: {e}")
            raise

    def editMessageCaption(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = 'html',
        caption_entities: Optional[list[Dict[str, Any]]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Edit captions of messages.

        Args:
            chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat.
            message_id: Required if inline_message_id is not specified. Identifier of the message to edit.
            inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message.
            caption: New caption of the message, 0-1024 characters after entities parsing.
            parse_mode: Mode for parsing entities in the caption.
            caption_entities: A JSON-serialized list of special entities that appear in the caption.
            reply_markup: A JSON-serialized object for an inline keyboard.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If neither message_id/chat_id nor inline_message_id is provided.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not (message_id and chat_id) and not inline_message_id:
            raise ValueError("Either (chat_id and message_id) or inline_message_id must be provided.")

        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'caption': caption,
            'parse_mode': parse_mode,
            'caption_entities': caption_entities,
            'reply_markup': reply_markup,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        if isinstance(clean_payload.get('reply_markup'), dict):
            clean_payload['reply_markup'] = json.dumps(clean_payload['reply_markup'])
        if isinstance(clean_payload.get('caption_entities'), list):
            clean_payload['caption_entities'] = json.dumps(clean_payload['caption_entities'])

        try:
            return self.request(
                method="editMessageCaption",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to edit message caption. Error: {e}")
            raise

    def editMessageLiveLocation(
        self,
        latitude: float,
        longitude: float,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        live_period: Optional[int] = None,
        horizontal_accuracy: Optional[float] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Edit live location messages.

        Args:
            latitude: Latitude of new location.
            longitude: Longitude of new location.
            chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat.
            message_id: Required if inline_message_id is not specified. Identifier of the message to edit.
            inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message.
            live_period: New period in seconds for which the location can be updated, should be between 60 and 86400.
            horizontal_accuracy: The radius of a circle around the unrounded latitude and longitude, measured in meters.
            heading: Direction in which the user is moving, in degrees.
            proximity_alert_radius: The maximum distance for proximity alerts about approaching another chat member.
            reply_markup: A JSON-serialized object for an inline keyboard.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If neither message_id/chat_id nor inline_message_id is provided, or if latitude/longitude are missing.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not (message_id and chat_id) and not inline_message_id:
            raise ValueError("Either (chat_id and message_id) or inline_message_id must be provided.")
        if latitude is None or longitude is None:
            raise ValueError("latitude and longitude are required.")

        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'latitude': latitude,
            'longitude': longitude,
            'live_period': live_period,
            'horizontal_accuracy': horizontal_accuracy,
            'heading': heading,
            'proximity_alert_radius': proximity_alert_radius,
            'reply_markup': reply_markup,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        if isinstance(clean_payload.get('reply_markup'), dict):
            clean_payload['reply_markup'] = json.dumps(clean_payload['reply_markup'])

        try:
            return self.request(
                method="editMessageLiveLocation",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to edit live location. Error: {e}")
            raise

    def editMessageMedia(
        self,
        media: Dict[str, Any],
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Edit messages with content of a media type.

        Args:
            media: A JSON-serialized object for a new media content of the message.
            chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat.
            message_id: Required if inline_message_id is not specified. Identifier of the message to edit.
            inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message.
            reply_markup: A JSON-serialized object for an inline keyboard.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If 'media' is missing, or if neither message_id/chat_id nor inline_message_id is provided.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not media:
            raise ValueError("media is required.")
        if not (message_id and chat_id) and not inline_message_id:
            raise ValueError("Either (chat_id and message_id) or inline_message_id must be provided.")

        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'media': media,
            'reply_markup': reply_markup,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        # Telegram API expects 'media' to be a JSON string
        if isinstance(clean_payload.get('media'), dict):
            clean_payload['media'] = json.dumps(clean_payload['media'])
        if isinstance(clean_payload.get('reply_markup'), dict):
            clean_payload['reply_markup'] = json.dumps(clean_payload['reply_markup'])

        # This method might require multipart/form-data if 'media' involves file uploads.
        # However, the 'media' parameter itself is a JSON object describing the media.
        # The file content usually comes in a separate 'file' field or as part of the 'media' object itself
        # with 'attach://<file_id>'. For simplicity, assuming 'media' is purely JSON.
        # If files are to be uploaded directly, the 'request' method would need to handle 'files' parameter for 'editMessageMedia'.
        # For now, we'll assume media references existing files or URLs.

        try:
            return self.request(
                method="editMessageMedia",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to edit message media. Error: {e}")
            raise

    def editMessageReplyMarkup(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Edit only the reply markup of messages.

        Args:
            chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat.
            message_id: Required if inline_message_id is not specified. Identifier of the message to edit.
            inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message.
            reply_markup: A JSON-serialized object for an inline keyboard.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If neither message_id/chat_id nor inline_message_id is provided.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not (message_id and chat_id) and not inline_message_id:
            raise ValueError("Either (chat_id and message_id) or inline_message_id must be provided.")

        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'reply_markup': reply_markup,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        if isinstance(clean_payload.get('reply_markup'), dict):
            clean_payload['reply_markup'] = json.dumps(clean_payload['reply_markup'])

        try:
            return self.request(
                method="editMessageReplyMarkup",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to edit message reply markup. Error: {e}")
            raise

    def editMessageText(
        self,
        text: str,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        parse_mode: Optional[str] = 'html',
        entities: Optional[list[Dict[str, Any]]] = None,
        link_preview_options: Optional[Dict[str, Any]] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Edit text messages.

        Args:
            text: New text of the message, 1-4096 characters after entities parsing.
            chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat.
            message_id: Required if inline_message_id is not specified. Identifier of the message to edit.
            inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message.
            parse_mode: Mode for parsing entities in the message text.
            entities: A JSON-serialized list of special entities that appear in message text.
            link_preview_options: A JSON-serialized object for link preview options.
            reply_markup: A JSON-serialized object for an inline keyboard.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If 'text' is empty, or if neither message_id/chat_id nor inline_message_id is provided.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not text.strip():
            raise ValueError("text cannot be empty.")
        if not (message_id and chat_id) and not inline_message_id:
            raise ValueError("Either (chat_id and message_id) or inline_message_id must be provided.")

        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'text': format_text(text),
            'parse_mode': parse_mode,
            'entities': entities,
            'link_preview_options': link_preview_options,
            'reply_markup': reply_markup,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        if isinstance(clean_payload.get('reply_markup'), dict):
            clean_payload['reply_markup'] = json.dumps(clean_payload['reply_markup'])
        if isinstance(clean_payload.get('entities'), list):
            clean_payload['entities'] = json.dumps(clean_payload['entities'])
        if isinstance(clean_payload.get('link_preview_options'), dict):
            clean_payload['link_preview_options'] = json.dumps(clean_payload['link_preview_options'])

        try:
            return self.request(
                method="editMessageText",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to edit message text. Error: {e}")
            raise

    def stopMessageLiveLocation(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Stop updating a live location message before live_period expires.

        Args:
            chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat.
            message_id: Required if inline_message_id is not specified. Identifier of the message to edit.
            inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message.
            reply_markup: A JSON-serialized object for an inline keyboard.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If neither message_id/chat_id nor inline_message_id is provided.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not (message_id and chat_id) and not inline_message_id:
            raise ValueError("Either (chat_id and message_id) or inline_message_id must be provided.")

        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            'inline_message_id': inline_message_id,
            'reply_markup': reply_markup,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        if isinstance(clean_payload.get('reply_markup'), dict):
            clean_payload['reply_markup'] = json.dumps(clean_payload['reply_markup'])

        try:
            return self.request(
                method="stopMessageLiveLocation",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to stop live location. Error: {e}")
            raise

    def stopPoll(
        self,
        chat_id: Union[int, str],
        message_id: int,
        reply_markup: Optional[Dict[str, Any]] = None,
        return_response: bool = True,
        **kwargs: Any
    ) -> Optional[requests.Response]:
        """
        Stop a poll which was sent by the bot.

        Args:
            chat_id: Unique identifier for the target chat.
            message_id: Identifier of the original message with the poll.
            reply_markup: A JSON-serialized object for an inline keyboard.
            return_response: Whether to return the raw response object.
            **kwargs: Additional API parameters.

        Returns:
            requests.Response if return_response=True, None otherwise.

        Raises:
            ValueError: If required parameters are missing.
            requests.exceptions.RequestException: For request-related errors.
        """
        if not chat_id:
            raise ValueError("chat_id is required.")
        if not message_id:
            raise ValueError("message_id is required.")

        payload = {
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': reply_markup,
            **kwargs
        }

        clean_payload = {k: v for k, v in payload.items() if v is not None}

        if isinstance(clean_payload.get('reply_markup'), dict):
            clean_payload['reply_markup'] = json.dumps(clean_payload['reply_markup'])

        try:
            return self.request(
                method="stopPoll",
                payload=clean_payload,
                return_response=return_response
            )
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to stop poll in chat {chat_id}, message {message_id}. Error: {e}")
            raise