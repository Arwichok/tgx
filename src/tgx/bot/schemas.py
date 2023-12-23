from __future__ import annotations
from typing import List, Optional, Union

from ._base import Schema, field




class Update(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This [object](#available-types) represents an incoming update.
    At most **one** of the optional parameters can be present in any given
    update.
    """
    update_id: int = field()
    """The update's unique identifier. Update identifiers start from a
    certain positive number and increase sequentially. This ID becomes
    especially handy if you're using webhooks, since it allows you to
    ignore repeated updates or to restore the correct update sequence,
    should they get out of order. If there are no new updates for at least
    a week, then identifier of the next update will be chosen randomly
    instead of sequentially."""
    message: Optional[Message] = field(default=None)
    """Optional. New incoming message of any kind - text, photo, sticker,
    etc."""
    edited_message: Optional[Message] = field(default=None)
    """Optional. New version of a message that is known to the bot and was
    edited"""
    channel_post: Optional[Message] = field(default=None)
    """Optional. New incoming channel post of any kind - text, photo,
    sticker, etc."""
    edited_channel_post: Optional[Message] = field(default=None)
    """Optional. New version of a channel post that is known to the bot and
    was edited"""
    inline_query: Optional[InlineQuery] = field(default=None)
    """Optional. New incoming inline query"""
    chosen_inline_result: Optional[ChosenInlineResult] = field(default=None)
    """Optional. The result of an inline query that was chosen by a user and
    sent to their chat partner. Please see our documentation on the
    feedback collecting for details on how to enable these updates for
    your bot."""
    callback_query: Optional[CallbackQuery] = field(default=None)
    """Optional. New incoming callback query"""
    shipping_query: Optional[ShippingQuery] = field(default=None)
    """Optional. New incoming shipping query. Only for invoices with flexible
    price"""
    pre_checkout_query: Optional[PreCheckoutQuery] = field(default=None)
    """Optional. New incoming pre-checkout query. Contains full information
    about checkout"""
    poll: Optional[Poll] = field(default=None)
    """Optional. New poll state. Bots receive only updates about stopped
    polls and polls, which are sent by the bot"""
    poll_answer: Optional[PollAnswer] = field(default=None)
    """Optional. A user changed their answer in a non-anonymous poll. Bots
    receive new votes only in polls that were sent by the bot itself."""
    my_chat_member: Optional[ChatMemberUpdated] = field(default=None)
    """Optional. The bot's chat member status was updated in a chat. For
    private chats, this update is received only when the bot is blocked or
    unblocked by the user."""
    chat_member: Optional[ChatMemberUpdated] = field(default=None)
    """Optional. A chat member's status was updated in a chat. The bot must
    be an administrator in the chat and must explicitly specify
    “chat_member” in the list of allowed_updates to receive these updates."""
    chat_join_request: Optional[ChatJoinRequest] = field(default=None)
    """Optional. A request to join the chat has been sent. The bot must have
    the can_invite_users administrator right in the chat to receive these
    updates."""




class WebhookInfo(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Describes the current status of a webhook.
    """
    url: str = field()
    """Webhook URL, may be empty if webhook is not set up"""
    has_custom_certificate: bool = field()
    """True, if a custom certificate was provided for webhook certificate
    checks"""
    pending_update_count: int = field()
    """Number of updates awaiting delivery"""
    ip_address: Optional[str] = field(default=None)
    """Optional. Currently used webhook IP address"""
    last_error_date: Optional[int] = field(default=None)
    """Optional. Unix time for the most recent error that happened when
    trying to deliver an update via webhook"""
    last_error_message: Optional[str] = field(default=None)
    """Optional. Error message in human-readable format for the most recent
    error that happened when trying to deliver an update via webhook"""
    last_synchronization_error_date: Optional[int] = field(default=None)
    """Optional. Unix time of the most recent error that happened when trying
    to synchronize available updates with Telegram datacenters"""
    max_connections: Optional[int] = field(default=None)
    """Optional. The maximum allowed number of simultaneous HTTPS connections
    to the webhook for update delivery"""
    allowed_updates: Optional[List[str]] = field(default=None)
    """Optional. A list of update types the bot is subscribed to. Defaults to
    all update types except chat_member"""




class User(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a Telegram user or bot.
    """
    id: int = field()
    """Unique identifier for this user or bot. This number may have more than
    32 significant bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it has at most 52
    significant bits, so a 64-bit integer or double-precision float type
    are safe for storing this identifier."""
    is_bot: bool = field()
    """True, if this user is a bot"""
    first_name: str = field()
    """User's or bot's first name"""
    last_name: Optional[str] = field(default=None)
    """Optional. User's or bot's last name"""
    username: Optional[str] = field(default=None)
    """Optional. User's or bot's username"""
    language_code: Optional[str] = field(default=None)
    """Optional. IETF language tag of the user's language"""
    is_premium: Optional[bool] = field(default=None)
    """Optional. True, if this user is a Telegram Premium user"""
    added_to_attachment_menu: Optional[bool] = field(default=None)
    """Optional. True, if this user added the bot to the attachment menu"""
    can_join_groups: Optional[bool] = field(default=None)
    """Optional. True, if the bot can be invited to groups. Returned only in
    getMe."""
    can_read_all_group_messages: Optional[bool] = field(default=None)
    """Optional. True, if privacy mode is disabled for the bot. Returned only
    in getMe."""
    supports_inline_queries: Optional[bool] = field(default=None)
    """Optional. True, if the bot supports inline queries. Returned only in
    getMe."""




class Chat(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a chat.
    """
    id: int = field()
    """Unique identifier for this chat. This number may have more than 32
    significant bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it has at most 52
    significant bits, so a signed 64-bit integer or double-precision float
    type are safe for storing this identifier."""
    type: str = field()
    """Type of chat, can be either “private”, “group”, “supergroup” or
    “channel”"""
    title: Optional[str] = field(default=None)
    """Optional. Title, for supergroups, channels and group chats"""
    username: Optional[str] = field(default=None)
    """Optional. Username, for private chats, supergroups and channels if
    available"""
    first_name: Optional[str] = field(default=None)
    """Optional. First name of the other party in a private chat"""
    last_name: Optional[str] = field(default=None)
    """Optional. Last name of the other party in a private chat"""
    is_forum: Optional[bool] = field(default=None)
    """Optional. True, if the supergroup chat is a forum (has topics enabled)"""
    photo: Optional[ChatPhoto] = field(default=None)
    """Optional. Chat photo. Returned only in getChat."""
    active_usernames: Optional[List[str]] = field(default=None)
    """Optional. If non-empty, the list of all active chat usernames; for
    private chats, supergroups and channels. Returned only in getChat."""
    emoji_status_custom_emoji_id: Optional[str] = field(default=None)
    """Optional. Custom emoji identifier of emoji status of the other party
    in a private chat. Returned only in getChat."""
    emoji_status_expiration_date: Optional[int] = field(default=None)
    """Optional. Expiration date of the emoji status of the other party in a
    private chat in Unix time, if any. Returned only in getChat."""
    bio: Optional[str] = field(default=None)
    """Optional. Bio of the other party in a private chat. Returned only in
    getChat."""
    has_private_forwards: Optional[bool] = field(default=None)
    """Optional. True, if privacy settings of the other party in the private
    chat allows to use tg://user?id=<user_id> links only in chats with the
    user. Returned only in getChat."""
    has_restricted_voice_and_video_messages: Optional[bool] = field(default=None)
    """Optional. True, if the privacy settings of the other party restrict
    sending voice and video note messages in the private chat. Returned
    only in getChat."""
    join_to_send_messages: Optional[bool] = field(default=None)
    """Optional. True, if users need to join the supergroup before they can
    send messages. Returned only in getChat."""
    join_by_request: Optional[bool] = field(default=None)
    """Optional. True, if all users directly joining the supergroup need to
    be approved by supergroup administrators. Returned only in getChat."""
    description: Optional[str] = field(default=None)
    """Optional. Description, for groups, supergroups and channel chats.
    Returned only in getChat."""
    invite_link: Optional[str] = field(default=None)
    """Optional. Primary invite link, for groups, supergroups and channel
    chats. Returned only in getChat."""
    pinned_message: Optional[Message] = field(default=None)
    """Optional. The most recent pinned message (by sending date). Returned
    only in getChat."""
    permissions: Optional[ChatPermissions] = field(default=None)
    """Optional. Default chat member permissions, for groups and supergroups.
    Returned only in getChat."""
    slow_mode_delay: Optional[int] = field(default=None)
    """Optional. For supergroups, the minimum allowed delay between
    consecutive messages sent by each unpriviledged user; in seconds.
    Returned only in getChat."""
    message_auto_delete_time: Optional[int] = field(default=None)
    """Optional. The time after which all messages sent to the chat will be
    automatically deleted; in seconds. Returned only in getChat."""
    has_aggressive_anti_spam_enabled: Optional[bool] = field(default=None)
    """Optional. True, if aggressive anti-spam checks are enabled in the
    supergroup. The field is only available to chat administrators.
    Returned only in getChat."""
    has_hidden_members: Optional[bool] = field(default=None)
    """Optional. True, if non-administrators can only get the list of bots
    and administrators in the chat. Returned only in getChat."""
    has_protected_content: Optional[bool] = field(default=None)
    """Optional. True, if messages from the chat can't be forwarded to other
    chats. Returned only in getChat."""
    sticker_set_name: Optional[str] = field(default=None)
    """Optional. For supergroups, name of group sticker set. Returned only in
    getChat."""
    can_set_sticker_set: Optional[bool] = field(default=None)
    """Optional. True, if the bot can change the group sticker set. Returned
    only in getChat."""
    linked_chat_id: Optional[int] = field(default=None)
    """Optional. Unique identifier for the linked chat, i.e. the discussion
    group identifier for a channel and vice versa; for supergroups and
    channel chats. This identifier may be greater than 32 bits and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it is smaller than 52 bits, so a signed 64 bit
    integer or double-precision float type are safe for storing this
    identifier. Returned only in getChat."""
    location: Optional[ChatLocation] = field(default=None)
    """Optional. For supergroups, the location to which the supergroup is
    connected. Returned only in getChat."""




class Message(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a message.
    """
    message_id: int = field()
    """Unique message identifier inside this chat"""
    date: int = field()
    """Date the message was sent in Unix time"""
    chat: Chat = field()
    """Conversation the message belongs to"""
    message_thread_id: Optional[int] = field(default=None)
    """Optional. Unique identifier of a message thread to which the message
    belongs; for supergroups only"""
    from_: Optional[User] = field(name='from', default=None)
    """Optional. Sender of the message; empty for messages sent to channels.
    For backward compatibility, the field contains a fake sender user in
    non-channel chats, if the message was sent on behalf of a chat."""
    sender_chat: Optional[Chat] = field(default=None)
    """Optional. Sender of the message, sent on behalf of a chat. For
    example, the channel itself for channel posts, the supergroup itself
    for messages from anonymous group administrators, the linked channel
    for messages automatically forwarded to the discussion group. For
    backward compatibility, the field from contains a fake sender user in
    non-channel chats, if the message was sent on behalf of a chat."""
    forward_from: Optional[User] = field(default=None)
    """Optional. For forwarded messages, sender of the original message"""
    forward_from_chat: Optional[Chat] = field(default=None)
    """Optional. For messages forwarded from channels or from anonymous
    administrators, information about the original sender chat"""
    forward_from_message_id: Optional[int] = field(default=None)
    """Optional. For messages forwarded from channels, identifier of the
    original message in the channel"""
    forward_signature: Optional[str] = field(default=None)
    """Optional. For forwarded messages that were originally sent in channels
    or by an anonymous chat administrator, signature of the message sender
    if present"""
    forward_sender_name: Optional[str] = field(default=None)
    """Optional. Sender's name for messages forwarded from users who disallow
    adding a link to their account in forwarded messages"""
    forward_date: Optional[int] = field(default=None)
    """Optional. For forwarded messages, date the original message was sent
    in Unix time"""
    is_topic_message: Optional[bool] = field(default=None)
    """Optional. True, if the message is sent to a forum topic"""
    is_automatic_forward: Optional[bool] = field(default=None)
    """Optional. True, if the message is a channel post that was
    automatically forwarded to the connected discussion group"""
    reply_to_message: Optional[Message] = field(default=None)
    """Optional. For replies, the original message. Note that the Message
    object in this field will not contain further reply_to_message fields
    even if it itself is a reply."""
    via_bot: Optional[User] = field(default=None)
    """Optional. Bot through which the message was sent"""
    edit_date: Optional[int] = field(default=None)
    """Optional. Date the message was last edited in Unix time"""
    has_protected_content: Optional[bool] = field(default=None)
    """Optional. True, if the message can't be forwarded"""
    media_group_id: Optional[str] = field(default=None)
    """Optional. The unique identifier of a media message group this message
    belongs to"""
    author_signature: Optional[str] = field(default=None)
    """Optional. Signature of the post author for messages in channels, or
    the custom title of an anonymous group administrator"""
    text: Optional[str] = field(default=None)
    """Optional. For text messages, the actual UTF-8 text of the message"""
    entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. For text messages, special entities like usernames, URLs,
    bot commands, etc. that appear in the text"""
    animation: Optional[Animation] = field(default=None)
    """Optional. Message is an animation, information about the animation.
    For backward compatibility, when this field is set, the document field
    will also be set"""
    audio: Optional[Audio] = field(default=None)
    """Optional. Message is an audio file, information about the file"""
    document: Optional[Document] = field(default=None)
    """Optional. Message is a general file, information about the file"""
    photo: Optional[List[PhotoSize]] = field(default=None)
    """Optional. Message is a photo, available sizes of the photo"""
    sticker: Optional[Sticker] = field(default=None)
    """Optional. Message is a sticker, information about the sticker"""
    story: Optional[Story] = field(default=None)
    """Optional. Message is a forwarded story"""
    video: Optional[Video] = field(default=None)
    """Optional. Message is a video, information about the video"""
    video_note: Optional[VideoNote] = field(default=None)
    """Optional. Message is a video note, information about the video message"""
    voice: Optional[Voice] = field(default=None)
    """Optional. Message is a voice message, information about the file"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption for the animation, audio, document, photo, video or
    voice"""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. For messages with a caption, special entities like
    usernames, URLs, bot commands, etc. that appear in the caption"""
    has_media_spoiler: Optional[bool] = field(default=None)
    """Optional. True, if the message media is covered by a spoiler animation"""
    contact: Optional[Contact] = field(default=None)
    """Optional. Message is a shared contact, information about the contact"""
    dice: Optional[Dice] = field(default=None)
    """Optional. Message is a dice with random value"""
    game: Optional[Game] = field(default=None)
    """Optional. Message is a game, information about the game. More about
    games »"""
    poll: Optional[Poll] = field(default=None)
    """Optional. Message is a native poll, information about the poll"""
    venue: Optional[Venue] = field(default=None)
    """Optional. Message is a venue, information about the venue. For
    backward compatibility, when this field is set, the location field
    will also be set"""
    location: Optional[Location] = field(default=None)
    """Optional. Message is a shared location, information about the location"""
    new_chat_members: Optional[List[User]] = field(default=None)
    """Optional. New members that were added to the group or supergroup and
    information about them (the bot itself may be one of these members)"""
    left_chat_member: Optional[User] = field(default=None)
    """Optional. A member was removed from the group, information about them
    (this member may be the bot itself)"""
    new_chat_title: Optional[str] = field(default=None)
    """Optional. A chat title was changed to this value"""
    new_chat_photo: Optional[List[PhotoSize]] = field(default=None)
    """Optional. A chat photo was change to this value"""
    delete_chat_photo: Optional[bool] = field(default=None)
    """Optional. Service message: the chat photo was deleted"""
    group_chat_created: Optional[bool] = field(default=None)
    """Optional. Service message: the group has been created"""
    supergroup_chat_created: Optional[bool] = field(default=None)
    """Optional. Service message: the supergroup has been created. This field
    can't be received in a message coming through updates, because bot
    can't be a member of a supergroup when it is created. It can only be
    found in reply_to_message if someone replies to a very first message
    in a directly created supergroup."""
    channel_chat_created: Optional[bool] = field(default=None)
    """Optional. Service message: the channel has been created. This field
    can't be received in a message coming through updates, because bot
    can't be a member of a channel when it is created. It can only be
    found in reply_to_message if someone replies to a very first message
    in a channel."""
    message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged] = field(default=None)
    """Optional. Service message: auto-delete timer settings changed in the
    chat"""
    migrate_to_chat_id: Optional[int] = field(default=None)
    """Optional. The group has been migrated to a supergroup with the
    specified identifier. This number may have more than 32 significant
    bits and some programming languages may have difficulty/silent defects
    in interpreting it. But it has at most 52 significant bits, so a
    signed 64-bit integer or double-precision float type are safe for
    storing this identifier."""
    migrate_from_chat_id: Optional[int] = field(default=None)
    """Optional. The supergroup has been migrated from a group with the
    specified identifier. This number may have more than 32 significant
    bits and some programming languages may have difficulty/silent defects
    in interpreting it. But it has at most 52 significant bits, so a
    signed 64-bit integer or double-precision float type are safe for
    storing this identifier."""
    pinned_message: Optional[Message] = field(default=None)
    """Optional. Specified message was pinned. Note that the Message object
    in this field will not contain further reply_to_message fields even if
    it is itself a reply."""
    invoice: Optional[Invoice] = field(default=None)
    """Optional. Message is an invoice for a payment, information about the
    invoice. More about payments »"""
    successful_payment: Optional[SuccessfulPayment] = field(default=None)
    """Optional. Message is a service message about a successful payment,
    information about the payment. More about payments »"""
    user_shared: Optional[UserShared] = field(default=None)
    """Optional. Service message: a user was shared with the bot"""
    chat_shared: Optional[ChatShared] = field(default=None)
    """Optional. Service message: a chat was shared with the bot"""
    connected_website: Optional[str] = field(default=None)
    """Optional. The domain name of the website on which the user has logged
    in. More about Telegram Login »"""
    write_access_allowed: Optional[WriteAccessAllowed] = field(default=None)
    """Optional. Service message: the user allowed the bot to write messages
    after adding it to the attachment or side menu, launching a Web App
    from a link, or accepting an explicit request from a Web App sent by
    the method requestWriteAccess"""
    passport_data: Optional[PassportData] = field(default=None)
    """Optional. Telegram Passport data"""
    proximity_alert_triggered: Optional[ProximityAlertTriggered] = field(default=None)
    """Optional. Service message. A user in the chat triggered another user's
    proximity alert while sharing Live Location."""
    forum_topic_created: Optional[ForumTopicCreated] = field(default=None)
    """Optional. Service message: forum topic created"""
    forum_topic_edited: Optional[ForumTopicEdited] = field(default=None)
    """Optional. Service message: forum topic edited"""
    forum_topic_closed: Optional[ForumTopicClosed] = field(default=None)
    """Optional. Service message: forum topic closed"""
    forum_topic_reopened: Optional[ForumTopicReopened] = field(default=None)
    """Optional. Service message: forum topic reopened"""
    general_forum_topic_hidden: Optional[GeneralForumTopicHidden] = field(default=None)
    """Optional. Service message: the 'General' forum topic hidden"""
    general_forum_topic_unhidden: Optional[GeneralForumTopicUnhidden] = field(default=None)
    """Optional. Service message: the 'General' forum topic unhidden"""
    video_chat_scheduled: Optional[VideoChatScheduled] = field(default=None)
    """Optional. Service message: video chat scheduled"""
    video_chat_started: Optional[VideoChatStarted] = field(default=None)
    """Optional. Service message: video chat started"""
    video_chat_ended: Optional[VideoChatEnded] = field(default=None)
    """Optional. Service message: video chat ended"""
    video_chat_participants_invited: Optional[VideoChatParticipantsInvited] = field(default=None)
    """Optional. Service message: new participants invited to a video chat"""
    web_app_data: Optional[WebAppData] = field(default=None)
    """Optional. Service message: data sent by a Web App"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message. login_url buttons
    are represented as ordinary url buttons."""




class MessageId(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a unique message identifier.
    """
    message_id: int = field()
    """Unique message identifier"""




class MessageEntity(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents one special entity in a text message. For
    example, hashtags, usernames, URLs, etc.
    """
    type: str = field()
    """Type of the entity. Currently, can be “mention” (@username), “hashtag”
    (#hashtag), “cashtag” ($USD), “bot_command” (/start@jobs_bot), “url”
    (https://telegram.org), “email” (do-not-reply@telegram.org),
    “phone_number” (+1-212-555-0123), “bold” (bold text), “italic” (italic
    text), “underline” (underlined text), “strikethrough” (strikethrough
    text), “spoiler” (spoiler message), “code” (monowidth string), “pre”
    (monowidth block), “text_link” (for clickable text URLs),
    “text_mention” (for users without usernames), “custom_emoji” (for
    inline custom emoji stickers)"""
    offset: int = field()
    """Offset in UTF-16 code units to the start of the entity"""
    length: int = field()
    """Length of the entity in UTF-16 code units"""
    url: Optional[str] = field(default=None)
    """Optional. For “text_link” only, URL that will be opened after user
    taps on the text"""
    user: Optional[User] = field(default=None)
    """Optional. For “text_mention” only, the mentioned user"""
    language: Optional[str] = field(default=None)
    """Optional. For “pre” only, the programming language of the entity text"""
    custom_emoji_id: Optional[str] = field(default=None)
    """Optional. For “custom_emoji” only, unique identifier of the custom
    emoji. Use getCustomEmojiStickers to get full information about the
    sticker"""




class PhotoSize(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents one size of a photo or a [file](#document) /
    [sticker](#sticker) thumbnail.
    """
    file_id: str = field()
    """Identifier for this file, which can be used to download or reuse the
    file"""
    file_unique_id: str = field()
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots. Can't be used to download or reuse the
    file."""
    width: int = field()
    """Photo width"""
    height: int = field()
    """Photo height"""
    file_size: Optional[int] = field(default=None)
    """Optional. File size in bytes"""




class Animation(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents an animation file (GIF or H.264/MPEG-4 AVC
    video without sound).
    """
    file_id: str = field()
    """Identifier for this file, which can be used to download or reuse the
    file"""
    file_unique_id: str = field()
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots. Can't be used to download or reuse the
    file."""
    width: int = field()
    """Video width as defined by sender"""
    height: int = field()
    """Video height as defined by sender"""
    duration: int = field()
    """Duration of the video in seconds as defined by sender"""
    thumbnail: Optional[PhotoSize] = field(default=None)
    """Optional. Animation thumbnail as defined by sender"""
    file_name: Optional[str] = field(default=None)
    """Optional. Original animation filename as defined by sender"""
    mime_type: Optional[str] = field(default=None)
    """Optional. MIME type of the file as defined by sender"""
    file_size: Optional[int] = field(default=None)
    """Optional. File size in bytes. It can be bigger than 2^31 and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed
    64-bit integer or double-precision float type are safe for storing
    this value."""




class Audio(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents an audio file to be treated as music by the
    Telegram clients.
    """
    file_id: str = field()
    """Identifier for this file, which can be used to download or reuse the
    file"""
    file_unique_id: str = field()
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots. Can't be used to download or reuse the
    file."""
    duration: int = field()
    """Duration of the audio in seconds as defined by sender"""
    performer: Optional[str] = field(default=None)
    """Optional. Performer of the audio as defined by sender or by audio tags"""
    title: Optional[str] = field(default=None)
    """Optional. Title of the audio as defined by sender or by audio tags"""
    file_name: Optional[str] = field(default=None)
    """Optional. Original filename as defined by sender"""
    mime_type: Optional[str] = field(default=None)
    """Optional. MIME type of the file as defined by sender"""
    file_size: Optional[int] = field(default=None)
    """Optional. File size in bytes. It can be bigger than 2^31 and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed
    64-bit integer or double-precision float type are safe for storing
    this value."""
    thumbnail: Optional[PhotoSize] = field(default=None)
    """Optional. Thumbnail of the album cover to which the music file belongs"""




class Document(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a general file (as opposed to
    [photos](#photosize), [voice messages](#voice) and [audio
    files](#audio)).
    """
    file_id: str = field()
    """Identifier for this file, which can be used to download or reuse the
    file"""
    file_unique_id: str = field()
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots. Can't be used to download or reuse the
    file."""
    thumbnail: Optional[PhotoSize] = field(default=None)
    """Optional. Document thumbnail as defined by sender"""
    file_name: Optional[str] = field(default=None)
    """Optional. Original filename as defined by sender"""
    mime_type: Optional[str] = field(default=None)
    """Optional. MIME type of the file as defined by sender"""
    file_size: Optional[int] = field(default=None)
    """Optional. File size in bytes. It can be bigger than 2^31 and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed
    64-bit integer or double-precision float type are safe for storing
    this value."""




class Story(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a message about a forwarded story in the chat.
    Currently holds no information.
    """
    ...





class Video(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a video file.
    """
    file_id: str = field()
    """Identifier for this file, which can be used to download or reuse the
    file"""
    file_unique_id: str = field()
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots. Can't be used to download or reuse the
    file."""
    width: int = field()
    """Video width as defined by sender"""
    height: int = field()
    """Video height as defined by sender"""
    duration: int = field()
    """Duration of the video in seconds as defined by sender"""
    thumbnail: Optional[PhotoSize] = field(default=None)
    """Optional. Video thumbnail"""
    file_name: Optional[str] = field(default=None)
    """Optional. Original filename as defined by sender"""
    mime_type: Optional[str] = field(default=None)
    """Optional. MIME type of the file as defined by sender"""
    file_size: Optional[int] = field(default=None)
    """Optional. File size in bytes. It can be bigger than 2^31 and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed
    64-bit integer or double-precision float type are safe for storing
    this value."""




class VideoNote(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a [video
    message](https://telegram.org/blog/video-messages-and-telescope)
    (available in Telegram apps as of
    [v.4.0](https://telegram.org/blog/video-messages-and-telescope)).
    """
    file_id: str = field()
    """Identifier for this file, which can be used to download or reuse the
    file"""
    file_unique_id: str = field()
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots. Can't be used to download or reuse the
    file."""
    length: int = field()
    """Video width and height (diameter of the video message) as defined by
    sender"""
    duration: int = field()
    """Duration of the video in seconds as defined by sender"""
    thumbnail: Optional[PhotoSize] = field(default=None)
    """Optional. Video thumbnail"""
    file_size: Optional[int] = field(default=None)
    """Optional. File size in bytes"""




class Voice(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a voice note.
    """
    file_id: str = field()
    """Identifier for this file, which can be used to download or reuse the
    file"""
    file_unique_id: str = field()
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots. Can't be used to download or reuse the
    file."""
    duration: int = field()
    """Duration of the audio in seconds as defined by sender"""
    mime_type: Optional[str] = field(default=None)
    """Optional. MIME type of the file as defined by sender"""
    file_size: Optional[int] = field(default=None)
    """Optional. File size in bytes. It can be bigger than 2^31 and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed
    64-bit integer or double-precision float type are safe for storing
    this value."""




class Contact(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a phone contact.
    """
    phone_number: str = field()
    """Contact's phone number"""
    first_name: str = field()
    """Contact's first name"""
    last_name: Optional[str] = field(default=None)
    """Optional. Contact's last name"""
    user_id: Optional[int] = field(default=None)
    """Optional. Contact's user identifier in Telegram. This number may have
    more than 32 significant bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it has at most 52
    significant bits, so a 64-bit integer or double-precision float type
    are safe for storing this identifier."""
    vcard: Optional[str] = field(default=None)
    """Optional. Additional data about the contact in the form of a vCard"""




class Dice(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents an animated emoji that displays a random value.
    """
    emoji: str = field()
    """Emoji on which the dice throw animation is based"""
    value: int = field()
    """Value of the dice, 1-6 for “”, “” and “” base emoji, 1-5 for “” and “”
    base emoji, 1-64 for “” base emoji"""




class PollOption(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object contains information about one answer option in a poll.
    """
    text: str = field()
    """Option text, 1-100 characters"""
    voter_count: int = field()
    """Number of users that voted for this option"""




class PollAnswer(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents an answer of a user in a non-anonymous poll.
    """
    poll_id: str = field()
    """Unique poll identifier"""
    option_ids: List[int] = field()
    """0-based identifiers of chosen answer options. May be empty if the vote
    was retracted."""
    voter_chat: Optional[Chat] = field(default=None)
    """Optional. The chat that changed the answer to the poll, if the voter
    is anonymous"""
    user: Optional[User] = field(default=None)
    """Optional. The user that changed the answer to the poll, if the voter
    isn't anonymous"""




class Poll(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object contains information about a poll.
    """
    id: str = field()
    """Unique poll identifier"""
    question: str = field()
    """Poll question, 1-300 characters"""
    options: List[PollOption] = field()
    """List of poll options"""
    total_voter_count: int = field()
    """Total number of users that voted in the poll"""
    is_closed: bool = field()
    """True, if the poll is closed"""
    is_anonymous: bool = field()
    """True, if the poll is anonymous"""
    type: str = field()
    """Poll type, currently can be “regular” or “quiz”"""
    allows_multiple_answers: bool = field()
    """True, if the poll allows multiple answers"""
    correct_option_id: Optional[int] = field(default=None)
    """Optional. 0-based identifier of the correct answer option. Available
    only for polls in the quiz mode, which are closed, or was sent (not
    forwarded) by the bot or to the private chat with the bot."""
    explanation: Optional[str] = field(default=None)
    """Optional. Text that is shown when a user chooses an incorrect answer
    or taps on the lamp icon in a quiz-style poll, 0-200 characters"""
    explanation_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. Special entities like usernames, URLs, bot commands, etc.
    that appear in the explanation"""
    open_period: Optional[int] = field(default=None)
    """Optional. Amount of time in seconds the poll will be active after
    creation"""
    close_date: Optional[int] = field(default=None)
    """Optional. Point in time (Unix timestamp) when the poll will be
    automatically closed"""




class Location(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a point on the map.
    """
    longitude: float = field()
    """Longitude as defined by sender"""
    latitude: float = field()
    """Latitude as defined by sender"""
    horizontal_accuracy: Optional[float] = field(default=None)
    """Optional. The radius of uncertainty for the location, measured in
    meters; 0-1500"""
    live_period: Optional[int] = field(default=None)
    """Optional. Time relative to the message sending date, during which the
    location can be updated; in seconds. For active live locations only."""
    heading: Optional[int] = field(default=None)
    """Optional. The direction in which user is moving, in degrees; 1-360.
    For active live locations only."""
    proximity_alert_radius: Optional[int] = field(default=None)
    """Optional. The maximum distance for proximity alerts about approaching
    another chat member, in meters. For sent live locations only."""




class Venue(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a venue.
    """
    location: Location = field()
    """Venue location. Can't be a live location"""
    title: str = field()
    """Name of the venue"""
    address: str = field()
    """Address of the venue"""
    foursquare_id: Optional[str] = field(default=None)
    """Optional. Foursquare identifier of the venue"""
    foursquare_type: Optional[str] = field(default=None)
    """Optional. Foursquare type of the venue. (For example,
    “arts_entertainment/default”, “arts_entertainment/aquarium” or
    “food/icecream”.)"""
    google_place_id: Optional[str] = field(default=None)
    """Optional. Google Places identifier of the venue"""
    google_place_type: Optional[str] = field(default=None)
    """Optional. Google Places type of the venue. (See supported types.)"""




class WebAppData(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Describes data sent from a [Web App](/bots/webapps) to the bot.
    """
    data: str = field()
    """The data. Be aware that a bad client can send arbitrary data in this
    field."""
    button_text: str = field()
    """Text of the web_app keyboard button from which the Web App was opened.
    Be aware that a bad client can send arbitrary data in this field."""




class ProximityAlertTriggered(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents the content of a service message, sent whenever
    a user in the chat triggers a proximity alert set by another user.
    """
    traveler: User = field()
    """User that triggered the alert"""
    watcher: User = field()
    """User that set the alert"""
    distance: int = field()
    """The distance between the users"""




class MessageAutoDeleteTimerChanged(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a service message about a change in auto-delete
    timer settings.
    """
    message_auto_delete_time: int = field()
    """New auto-delete time for messages in the chat; in seconds"""




class ForumTopicCreated(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a service message about a new forum topic
    created in the chat.
    """
    name: str = field()
    """Name of the topic"""
    icon_color: int = field()
    """Color of the topic icon in RGB format"""
    icon_custom_emoji_id: Optional[str] = field(default=None)
    """Optional. Unique identifier of the custom emoji shown as the topic
    icon"""




class ForumTopicClosed(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a service message about a forum topic closed in
    the chat. Currently holds no information.
    """
    ...





class ForumTopicEdited(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a service message about an edited forum topic.
    """
    name: Optional[str] = field(default=None)
    """Optional. New name of the topic, if it was edited"""
    icon_custom_emoji_id: Optional[str] = field(default=None)
    """Optional. New identifier of the custom emoji shown as the topic icon,
    if it was edited; an empty string if the icon was removed"""




class ForumTopicReopened(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a service message about a forum topic reopened
    in the chat. Currently holds no information.
    """
    ...





class GeneralForumTopicHidden(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a service message about General forum topic
    hidden in the chat. Currently holds no information.
    """
    ...





class GeneralForumTopicUnhidden(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a service message about General forum topic
    unhidden in the chat. Currently holds no information.
    """
    ...





class UserShared(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object contains information about the user whose identifier was
    shared with the bot using a
    [KeyboardButtonRequestUser](#keyboardbuttonrequestuser) button.
    """
    request_id: int = field()
    """Identifier of the request"""
    user_id: int = field()
    """Identifier of the shared user. This number may have more than 32
    significant bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it has at most 52
    significant bits, so a 64-bit integer or double-precision float type
    are safe for storing this identifier. The bot may not have access to
    the user and could be unable to use this identifier, unless the user
    is already known to the bot by some other means."""




class ChatShared(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object contains information about the chat whose identifier was
    shared with the bot using a
    [KeyboardButtonRequestChat](#keyboardbuttonrequestchat) button.
    """
    request_id: int = field()
    """Identifier of the request"""
    chat_id: int = field()
    """Identifier of the shared chat. This number may have more than 32
    significant bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it has at most 52
    significant bits, so a 64-bit integer or double-precision float type
    are safe for storing this identifier. The bot may not have access to
    the chat and could be unable to use this identifier, unless the chat
    is already known to the bot by some other means."""




class WriteAccessAllowed(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a service message about a user allowing a bot
    to write messages after adding it to the attachment menu, launching a
    Web App from a link, or accepting an explicit request from a Web App
    sent by the method [requestWriteAccess](/bots/webapps#initializing-
    mini-apps).
    """
    from_request: Optional[bool] = field(default=None)
    """Optional. True, if the access was granted after the user accepted an
    explicit request from a Web App sent by the method requestWriteAccess"""
    web_app_name: Optional[str] = field(default=None)
    """Optional. Name of the Web App, if the access was granted when the Web
    App was launched from a link"""
    from_attachment_menu: Optional[bool] = field(default=None)
    """Optional. True, if the access was granted when the bot was added to
    the attachment or side menu"""




class VideoChatScheduled(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a service message about a video chat scheduled
    in the chat.
    """
    start_date: int = field()
    """Point in time (Unix timestamp) when the video chat is supposed to be
    started by a chat administrator"""




class VideoChatStarted(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a service message about a video chat started in
    the chat. Currently holds no information.
    """
    ...





class VideoChatEnded(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a service message about a video chat ended in
    the chat.
    """
    duration: int = field()
    """Video chat duration in seconds"""




class VideoChatParticipantsInvited(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a service message about new members invited to
    a video chat.
    """
    users: List[User] = field()
    """New members that were invited to the video chat"""




class UserProfilePhotos(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represent a user's profile pictures.
    """
    total_count: int = field()
    """Total number of profile pictures the target user has"""
    photos: List[PhotoSize] = field()
    """Requested profile pictures (in up to 4 sizes each)"""




class File(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a file ready to be downloaded. The file can be
    downloaded via the link
    `https://api.telegram.org/file/bot<token>/<file_path>`. It is
    guaranteed that the link will be valid for at least 1 hour. When the
    link expires, a new one can be requested by calling
    [getFile](#getfile).
    """
    file_id: str = field()
    """Identifier for this file, which can be used to download or reuse the
    file"""
    file_unique_id: str = field()
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots. Can't be used to download or reuse the
    file."""
    file_size: Optional[int] = field(default=None)
    """Optional. File size in bytes. It can be bigger than 2^31 and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a signed
    64-bit integer or double-precision float type are safe for storing
    this value."""
    file_path: Optional[str] = field(default=None)
    """Optional. File path. Use
    https://api.telegram.org/file/bot<token>/<file_path> to get the file."""




class WebAppInfo(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Describes a [Web App](/bots/webapps).
    """
    url: str = field()
    """An HTTPS URL of a Web App to be opened with additional data as
    specified in Initializing Web Apps"""




class ReplyKeyboardMarkup(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a [custom keyboard](/bots/features#keyboards)
    with reply options (see [Introduction to
    bots](/bots/features#keyboards) for details and examples).
    """
    keyboard: List[KeyboardButton] = field()
    """Array of button rows, each represented by an Array of KeyboardButton
    objects"""
    is_persistent: Optional[bool] = field(default=None)
    """Optional. Requests clients to always show the keyboard when the
    regular keyboard is hidden. Defaults to false, in which case the
    custom keyboard can be hidden and opened with a keyboard icon."""
    resize_keyboard: Optional[bool] = field(default=None)
    """Optional. Requests clients to resize the keyboard vertically for
    optimal fit (e.g., make the keyboard smaller if there are just two
    rows of buttons). Defaults to false, in which case the custom keyboard
    is always of the same height as the app's standard keyboard."""
    one_time_keyboard: Optional[bool] = field(default=None)
    """Optional. Requests clients to hide the keyboard as soon as it's been
    used. The keyboard will still be available, but clients will
    automatically display the usual letter-keyboard in the chat - the user
    can press a special button in the input field to see the custom
    keyboard again. Defaults to false."""
    input_field_placeholder: Optional[str] = field(default=None)
    """Optional. The placeholder to be shown in the input field when the
    keyboard is active; 1-64 characters"""
    selective: Optional[bool] = field(default=None)
    """Optional. Use this parameter if you want to show the keyboard to
    specific users only. Targets: 1) users that are @mentioned in the text
    of the Message object; 2) if the bot's message is a reply (has
    reply_to_message_id), sender of the original message.Example: A user
    requests to change the bot's language, bot replies to the request with
    a keyboard to select the new language. Other users in the group don't
    see the keyboard."""




class KeyboardButton(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents one button of the reply keyboard. For simple
    text buttons, *String* can be used instead of this object to specify
    the button text. The optional fields *web\_app*, *request\_user*,
    *request\_chat*, *request\_contact*, *request\_location*, and
    *request\_poll* are mutually exclusive.
    
    **Note:** *request\_contact* and *request\_location* options will only
    work in Telegram versions released after 9 April, 2016. Older clients
    will display *unsupported message*.
    **Note:** *request\_poll* option will only work in Telegram versions
    released after 23 January, 2020. Older clients will display
    *unsupported message*.
    **Note:** *web\_app* option will only work in Telegram versions
    released after 16 April, 2022. Older clients will display *unsupported
    message*.
    **Note:** *request\_user* and *request\_chat* options will only work
    in Telegram versions released after 3 February, 2023. Older clients
    will display *unsupported message*.
    """
    text: str = field()
    """Text of the button. If none of the optional fields are used, it will
    be sent as a message when the button is pressed"""
    request_user: Optional[KeyboardButtonRequestUser] = field(default=None)
    """Optional. If specified, pressing the button will open a list of
    suitable users. Tapping on any user will send their identifier to the
    bot in a “user_shared” service message. Available in private chats
    only."""
    request_chat: Optional[KeyboardButtonRequestChat] = field(default=None)
    """Optional. If specified, pressing the button will open a list of
    suitable chats. Tapping on a chat will send its identifier to the bot
    in a “chat_shared” service message. Available in private chats only."""
    request_contact: Optional[bool] = field(default=None)
    """Optional. If True, the user's phone number will be sent as a contact
    when the button is pressed. Available in private chats only."""
    request_location: Optional[bool] = field(default=None)
    """Optional. If True, the user's current location will be sent when the
    button is pressed. Available in private chats only."""
    request_poll: Optional[KeyboardButtonPollType] = field(default=None)
    """Optional. If specified, the user will be asked to create a poll and
    send it to the bot when the button is pressed. Available in private
    chats only."""
    web_app: Optional[WebAppInfo] = field(default=None)
    """Optional. If specified, the described Web App will be launched when
    the button is pressed. The Web App will be able to send a
    “web_app_data” service message. Available in private chats only."""




class KeyboardButtonRequestUser(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object defines the criteria used to request a suitable user. The
    identifier of the selected user will be shared with the bot when the
    corresponding button is pressed. [More about requesting users
    »](/bots/features#chat-and-user-selection)
    """
    request_id: int = field()
    """Signed 32-bit identifier of the request, which will be received back
    in the UserShared object. Must be unique within the message"""
    user_is_bot: Optional[bool] = field(default=None)
    """Optional. Pass True to request a bot, pass False to request a regular
    user. If not specified, no additional restrictions are applied."""
    user_is_premium: Optional[bool] = field(default=None)
    """Optional. Pass True to request a premium user, pass False to request a
    non-premium user. If not specified, no additional restrictions are
    applied."""




class KeyboardButtonRequestChat(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object defines the criteria used to request a suitable chat. The
    identifier of the selected chat will be shared with the bot when the
    corresponding button is pressed. [More about requesting chats
    »](/bots/features#chat-and-user-selection)
    """
    request_id: int = field()
    """Signed 32-bit identifier of the request, which will be received back
    in the ChatShared object. Must be unique within the message"""
    chat_is_channel: bool = field()
    """Pass True to request a channel chat, pass False to request a group or
    a supergroup chat."""
    chat_is_forum: Optional[bool] = field(default=None)
    """Optional. Pass True to request a forum supergroup, pass False to
    request a non-forum chat. If not specified, no additional restrictions
    are applied."""
    chat_has_username: Optional[bool] = field(default=None)
    """Optional. Pass True to request a supergroup or a channel with a
    username, pass False to request a chat without a username. If not
    specified, no additional restrictions are applied."""
    chat_is_created: Optional[bool] = field(default=None)
    """Optional. Pass True to request a chat owned by the user. Otherwise, no
    additional restrictions are applied."""
    user_administrator_rights: Optional[ChatAdministratorRights] = field(default=None)
    """Optional. A JSON-serialized object listing the required administrator
    rights of the user in the chat. The rights must be a superset of
    bot_administrator_rights. If not specified, no additional restrictions
    are applied."""
    bot_administrator_rights: Optional[ChatAdministratorRights] = field(default=None)
    """Optional. A JSON-serialized object listing the required administrator
    rights of the bot in the chat. The rights must be a subset of
    user_administrator_rights. If not specified, no additional
    restrictions are applied."""
    bot_is_member: Optional[bool] = field(default=None)
    """Optional. Pass True to request a chat with the bot as a member.
    Otherwise, no additional restrictions are applied."""




class KeyboardButtonPollType(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents type of a poll, which is allowed to be created
    and sent when the corresponding button is pressed.
    """
    type: Optional[str] = field(default=None)
    """Optional. If quiz is passed, the user will be allowed to create only
    polls in the quiz mode. If regular is passed, only regular polls will
    be allowed. Otherwise, the user will be allowed to create a poll of
    any type."""




class ReplyKeyboardRemove(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Upon receiving a message with this object, Telegram clients will
    remove the current custom keyboard and display the default letter-
    keyboard. By default, custom keyboards are displayed until a new
    keyboard is sent by a bot. An exception is made for one-time keyboards
    that are hidden immediately after the user presses a button (see
    [ReplyKeyboardMarkup](#replykeyboardmarkup)).
    """
    remove_keyboard: bool = field()
    """Requests clients to remove the custom keyboard (user will not be able
    to summon this keyboard; if you want to hide the keyboard from sight
    but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup)"""
    selective: Optional[bool] = field(default=None)
    """Optional. Use this parameter if you want to remove the keyboard for
    specific users only. Targets: 1) users that are @mentioned in the text
    of the Message object; 2) if the bot's message is a reply (has
    reply_to_message_id), sender of the original message.Example: A user
    votes in a poll, bot returns confirmation message in reply to the vote
    and removes the keyboard for that user, while still showing the
    keyboard with poll options to users who haven't voted yet."""




class InlineKeyboardMarkup(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents an [inline keyboard](/bots/features#inline-
    keyboards) that appears right next to the message it belongs to.
    
    **Note:** This will only work in Telegram versions released after 9
    April, 2016. Older clients will display *unsupported message*.
    """
    inline_keyboard: List[InlineKeyboardButton] = field()
    """Array of button rows, each represented by an Array of
    InlineKeyboardButton objects"""




class InlineKeyboardButton(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents one button of an inline keyboard. You **must**
    use exactly one of the optional fields.
    """
    text: str = field()
    """Label text on the button"""
    url: Optional[str] = field(default=None)
    """Optional. HTTP or tg:// URL to be opened when the button is pressed.
    Links tg://user?id=<user_id> can be used to mention a user by their ID
    without using a username, if this is allowed by their privacy
    settings."""
    callback_data: Optional[str] = field(default=None)
    """Optional. Data to be sent in a callback query to the bot when button
    is pressed, 1-64 bytes"""
    web_app: Optional[WebAppInfo] = field(default=None)
    """Optional. Description of the Web App that will be launched when the
    user presses the button. The Web App will be able to send an arbitrary
    message on behalf of the user using the method answerWebAppQuery.
    Available only in private chats between a user and the bot."""
    login_url: Optional[LoginUrl] = field(default=None)
    """Optional. An HTTPS URL used to automatically authorize the user. Can
    be used as a replacement for the Telegram Login Widget."""
    switch_inline_query: Optional[str] = field(default=None)
    """Optional. If set, pressing the button will prompt the user to select
    one of their chats, open that chat and insert the bot's username and
    the specified inline query in the input field. May be empty, in which
    case just the bot's username will be inserted."""
    switch_inline_query_current_chat: Optional[str] = field(default=None)
    """Optional. If set, pressing the button will insert the bot's username
    and the specified inline query in the current chat's input field. May
    be empty, in which case only the bot's username will be inserted.This
    offers a quick way for the user to open your bot in inline mode in the
    same chat - good for selecting something from multiple options."""
    switch_inline_query_chosen_chat: Optional[SwitchInlineQueryChosenChat] = field(default=None)
    """Optional. If set, pressing the button will prompt the user to select
    one of their chats of the specified type, open that chat and insert
    the bot's username and the specified inline query in the input field"""
    callback_game: Optional[CallbackGame] = field(default=None)
    """Optional. Description of the game that will be launched when the user
    presses the button.NOTE: This type of button must always be the first
    button in the first row."""
    pay: Optional[bool] = field(default=None)
    """Optional. Specify True, to send a Pay button.NOTE: This type of button
    must always be the first button in the first row and can only be used
    in invoice messages."""




class LoginUrl(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a parameter of the inline keyboard button used
    to automatically authorize a user. Serves as a great replacement for
    the [Telegram Login Widget](/widgets/login) when the user is coming
    from Telegram. All the user needs to do is tap/click a button and
    confirm that they want to log in:
    
    Telegram apps support these buttons as of [version
    5.7](https://telegram.org/blog/privacy-discussions-web-bots#meet-
    seamless-web-bots).
    """
    url: str = field()
    """An HTTPS URL to be opened with user authorization data added to the
    query string when the button is pressed. If the user refuses to
    provide authorization data, the original URL without information about
    the user will be opened. The data added is the same as described in
    Receiving authorization data.NOTE: You must always check the hash of
    the received data to verify the authentication and the integrity of
    the data as described in Checking authorization."""
    forward_text: Optional[str] = field(default=None)
    """Optional. New text of the button in forwarded messages."""
    bot_username: Optional[str] = field(default=None)
    """Optional. Username of a bot, which will be used for user
    authorization. See Setting up a bot for more details. If not
    specified, the current bot's username will be assumed. The url's
    domain must be the same as the domain linked with the bot. See Linking
    your domain to the bot for more details."""
    request_write_access: Optional[bool] = field(default=None)
    """Optional. Pass True to request the permission for your bot to send
    messages to the user."""




class SwitchInlineQueryChosenChat(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents an inline button that switches the current user
    to inline mode in a chosen chat, with an optional default inline
    query.
    """
    query: Optional[str] = field(default=None)
    """Optional. The default inline query to be inserted in the input field.
    If left empty, only the bot's username will be inserted"""
    allow_user_chats: Optional[bool] = field(default=None)
    """Optional. True, if private chats with users can be chosen"""
    allow_bot_chats: Optional[bool] = field(default=None)
    """Optional. True, if private chats with bots can be chosen"""
    allow_group_chats: Optional[bool] = field(default=None)
    """Optional. True, if group and supergroup chats can be chosen"""
    allow_channel_chats: Optional[bool] = field(default=None)
    """Optional. True, if channel chats can be chosen"""




class CallbackQuery(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents an incoming callback query from a callback
    button in an [inline keyboard](/bots/features#inline-keyboards). If
    the button that originated the query was attached to a message sent by
    the bot, the field *message* will be present. If the button was
    attached to a message sent via the bot (in [inline mode](#inline-
    mode)), the field *inline\_message\_id* will be present. Exactly one
    of the fields *data* or *game\_short\_name* will be present.
    """
    id: str = field()
    """Unique identifier for this query"""
    from_: User = field(name='from')
    """Sender"""
    chat_instance: str = field()
    """Global identifier, uniquely corresponding to the chat to which the
    message with the callback button was sent. Useful for high scores in
    games."""
    message: Optional[Message] = field(default=None)
    """Optional. Message with the callback button that originated the query.
    Note that message content and message date will not be available if
    the message is too old"""
    inline_message_id: Optional[str] = field(default=None)
    """Optional. Identifier of the message sent via the bot in inline mode,
    that originated the query."""
    data: Optional[str] = field(default=None)
    """Optional. Data associated with the callback button. Be aware that the
    message originated the query can contain no callback buttons with this
    data."""
    game_short_name: Optional[str] = field(default=None)
    """Optional. Short name of a Game to be returned, serves as the unique
    identifier for the game"""




class ForceReply(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Upon receiving a message with this object, Telegram clients will
    display a reply interface to the user (act as if the user has selected
    the bot's message and tapped 'Reply'). This can be extremely useful if
    you want to create user-friendly step-by-step interfaces without
    having to sacrifice [privacy mode](/bots/features#privacy-mode).
    """
    force_reply: bool = field()
    """Shows reply interface to the user, as if they manually selected the
    bot's message and tapped 'Reply'"""
    input_field_placeholder: Optional[str] = field(default=None)
    """Optional. The placeholder to be shown in the input field when the
    reply is active; 1-64 characters"""
    selective: Optional[bool] = field(default=None)
    """Optional. Use this parameter if you want to force reply from specific
    users only. Targets: 1) users that are @mentioned in the text of the
    Message object; 2) if the bot's message is a reply (has
    reply_to_message_id), sender of the original message."""




class ChatPhoto(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a chat photo.
    """
    small_file_id: str = field()
    """File identifier of small (160x160) chat photo. This file_id can be
    used only for photo download and only for as long as the photo is not
    changed."""
    small_file_unique_id: str = field()
    """Unique file identifier of small (160x160) chat photo, which is
    supposed to be the same over time and for different bots. Can't be
    used to download or reuse the file."""
    big_file_id: str = field()
    """File identifier of big (640x640) chat photo. This file_id can be used
    only for photo download and only for as long as the photo is not
    changed."""
    big_file_unique_id: str = field()
    """Unique file identifier of big (640x640) chat photo, which is supposed
    to be the same over time and for different bots. Can't be used to
    download or reuse the file."""




class ChatInviteLink(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Represents an invite link for a chat.
    """
    invite_link: str = field()
    """The invite link. If the link was created by another chat
    administrator, then the second part of the link will be replaced with
    “…”."""
    creator: User = field()
    """Creator of the link"""
    creates_join_request: bool = field()
    """True, if users joining the chat via the link need to be approved by
    chat administrators"""
    is_primary: bool = field()
    """True, if the link is primary"""
    is_revoked: bool = field()
    """True, if the link is revoked"""
    name: Optional[str] = field(default=None)
    """Optional. Invite link name"""
    expire_date: Optional[int] = field(default=None)
    """Optional. Point in time (Unix timestamp) when the link will expire or
    has been expired"""
    member_limit: Optional[int] = field(default=None)
    """Optional. The maximum number of users that can be members of the chat
    simultaneously after joining the chat via this invite link; 1-99999"""
    pending_join_request_count: Optional[int] = field(default=None)
    """Optional. Number of pending join requests created using this link"""




class ChatAdministratorRights(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Represents the rights of an administrator in a chat.
    """
    is_anonymous: bool = field()
    """True, if the user's presence in the chat is hidden"""
    can_manage_chat: bool = field()
    """True, if the administrator can access the chat event log, boost list
    in channels, see channel members, report spam messages, see anonymous
    administrators in supergroups and ignore slow mode. Implied by any
    other administrator privilege"""
    can_delete_messages: bool = field()
    """True, if the administrator can delete messages of other users"""
    can_manage_video_chats: bool = field()
    """True, if the administrator can manage video chats"""
    can_restrict_members: bool = field()
    """True, if the administrator can restrict, ban or unban chat members, or
    access supergroup statistics"""
    can_promote_members: bool = field()
    """True, if the administrator can add new administrators with a subset of
    their own privileges or demote administrators that they have promoted,
    directly or indirectly (promoted by administrators that were appointed
    by the user)"""
    can_change_info: bool = field()
    """True, if the user is allowed to change the chat title, photo and other
    settings"""
    can_invite_users: bool = field()
    """True, if the user is allowed to invite new users to the chat"""
    can_post_messages: Optional[bool] = field(default=None)
    """Optional. True, if the administrator can post messages in the channel,
    or access channel statistics; channels only"""
    can_edit_messages: Optional[bool] = field(default=None)
    """Optional. True, if the administrator can edit messages of other users
    and can pin messages; channels only"""
    can_pin_messages: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to pin messages; groups and
    supergroups only"""
    can_post_stories: Optional[bool] = field(default=None)
    """Optional. True, if the administrator can post stories in the channel;
    channels only"""
    can_edit_stories: Optional[bool] = field(default=None)
    """Optional. True, if the administrator can edit stories posted by other
    users; channels only"""
    can_delete_stories: Optional[bool] = field(default=None)
    """Optional. True, if the administrator can delete stories posted by
    other users; channels only"""
    can_manage_topics: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to create, rename, close, and
    reopen forum topics; supergroups only"""




class ChatMember(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object contains information about one member of a chat.
    Currently, the following 6 types of chat members are supported:
    """
    ...





class ChatMemberOwner(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="creator",
    tag_field="status"
):
    """
    Represents a [chat member](#chatmember) that owns the chat and has all
    administrator privileges.
    """
    user: User = field()
    """Information about the user"""
    is_anonymous: bool = field()
    """True, if the user's presence in the chat is hidden"""
    custom_title: Optional[str] = field(default=None)
    """Optional. Custom title for this user"""




class ChatMemberAdministrator(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="administrator",
    tag_field="status"
):
    """
    Represents a [chat member](#chatmember) that has some additional
    privileges.
    """
    user: User = field()
    """Information about the user"""
    can_be_edited: bool = field()
    """True, if the bot is allowed to edit administrator privileges of that
    user"""
    is_anonymous: bool = field()
    """True, if the user's presence in the chat is hidden"""
    can_manage_chat: bool = field()
    """True, if the administrator can access the chat event log, boost list
    in channels, see channel members, report spam messages, see anonymous
    administrators in supergroups and ignore slow mode. Implied by any
    other administrator privilege"""
    can_delete_messages: bool = field()
    """True, if the administrator can delete messages of other users"""
    can_manage_video_chats: bool = field()
    """True, if the administrator can manage video chats"""
    can_restrict_members: bool = field()
    """True, if the administrator can restrict, ban or unban chat members, or
    access supergroup statistics"""
    can_promote_members: bool = field()
    """True, if the administrator can add new administrators with a subset of
    their own privileges or demote administrators that they have promoted,
    directly or indirectly (promoted by administrators that were appointed
    by the user)"""
    can_change_info: bool = field()
    """True, if the user is allowed to change the chat title, photo and other
    settings"""
    can_invite_users: bool = field()
    """True, if the user is allowed to invite new users to the chat"""
    can_post_messages: Optional[bool] = field(default=None)
    """Optional. True, if the administrator can post messages in the channel,
    or access channel statistics; channels only"""
    can_edit_messages: Optional[bool] = field(default=None)
    """Optional. True, if the administrator can edit messages of other users
    and can pin messages; channels only"""
    can_pin_messages: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to pin messages; groups and
    supergroups only"""
    can_post_stories: Optional[bool] = field(default=None)
    """Optional. True, if the administrator can post stories in the channel;
    channels only"""
    can_edit_stories: Optional[bool] = field(default=None)
    """Optional. True, if the administrator can edit stories posted by other
    users; channels only"""
    can_delete_stories: Optional[bool] = field(default=None)
    """Optional. True, if the administrator can delete stories posted by
    other users; channels only"""
    can_manage_topics: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to create, rename, close, and
    reopen forum topics; supergroups only"""
    custom_title: Optional[str] = field(default=None)
    """Optional. Custom title for this user"""




class ChatMemberMember(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="member",
    tag_field="status"
):
    """
    Represents a [chat member](#chatmember) that has no additional
    privileges or restrictions.
    """
    user: User = field()
    """Information about the user"""




class ChatMemberRestricted(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="restricted",
    tag_field="status"
):
    """
    Represents a [chat member](#chatmember) that is under certain
    restrictions in the chat. Supergroups only.
    """
    user: User = field()
    """Information about the user"""
    is_member: bool = field()
    """True, if the user is a member of the chat at the moment of the request"""
    can_send_messages: bool = field()
    """True, if the user is allowed to send text messages, contacts,
    invoices, locations and venues"""
    can_send_audios: bool = field()
    """True, if the user is allowed to send audios"""
    can_send_documents: bool = field()
    """True, if the user is allowed to send documents"""
    can_send_photos: bool = field()
    """True, if the user is allowed to send photos"""
    can_send_videos: bool = field()
    """True, if the user is allowed to send videos"""
    can_send_video_notes: bool = field()
    """True, if the user is allowed to send video notes"""
    can_send_voice_notes: bool = field()
    """True, if the user is allowed to send voice notes"""
    can_send_polls: bool = field()
    """True, if the user is allowed to send polls"""
    can_send_other_messages: bool = field()
    """True, if the user is allowed to send animations, games, stickers and
    use inline bots"""
    can_add_web_page_previews: bool = field()
    """True, if the user is allowed to add web page previews to their
    messages"""
    can_change_info: bool = field()
    """True, if the user is allowed to change the chat title, photo and other
    settings"""
    can_invite_users: bool = field()
    """True, if the user is allowed to invite new users to the chat"""
    can_pin_messages: bool = field()
    """True, if the user is allowed to pin messages"""
    can_manage_topics: bool = field()
    """True, if the user is allowed to create forum topics"""
    until_date: int = field()
    """Date when restrictions will be lifted for this user; Unix time. If 0,
    then the user is restricted forever"""




class ChatMemberLeft(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="left",
    tag_field="status"
):
    """
    Represents a [chat member](#chatmember) that isn't currently a member
    of the chat, but may join it themselves.
    """
    user: User = field()
    """Information about the user"""




class ChatMemberBanned(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="kicked",
    tag_field="status"
):
    """
    Represents a [chat member](#chatmember) that was banned in the chat
    and can't return to the chat or view chat messages.
    """
    user: User = field()
    """Information about the user"""
    until_date: int = field()
    """Date when restrictions will be lifted for this user; Unix time. If 0,
    then the user is banned forever"""




class ChatMemberUpdated(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents changes in the status of a chat member.
    """
    chat: Chat = field()
    """Chat the user belongs to"""
    from_: User = field(name='from')
    """Performer of the action, which resulted in the change"""
    date: int = field()
    """Date the change was done in Unix time"""
    old_chat_member: ChatMember = field()
    """Previous information about the chat member"""
    new_chat_member: ChatMember = field()
    """New information about the chat member"""
    invite_link: Optional[ChatInviteLink] = field(default=None)
    """Optional. Chat invite link, which was used by the user to join the
    chat; for joining by invite link events only."""
    via_chat_folder_invite_link: Optional[bool] = field(default=None)
    """Optional. True, if the user joined the chat via a chat folder invite
    link"""




class ChatJoinRequest(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Represents a join request sent to a chat.
    """
    chat: Chat = field()
    """Chat to which the request was sent"""
    from_: User = field(name='from')
    """User that sent the join request"""
    user_chat_id: int = field()
    """Identifier of a private chat with the user who sent the join request.
    This number may have more than 32 significant bits and some
    programming languages may have difficulty/silent defects in
    interpreting it. But it has at most 52 significant bits, so a 64-bit
    integer or double-precision float type are safe for storing this
    identifier. The bot can use this identifier for 5 minutes to send
    messages until the join request is processed, assuming no other
    administrator contacted the user."""
    date: int = field()
    """Date the request was sent in Unix time"""
    bio: Optional[str] = field(default=None)
    """Optional. Bio of the user."""
    invite_link: Optional[ChatInviteLink] = field(default=None)
    """Optional. Chat invite link that was used by the user to send the join
    request"""




class ChatPermissions(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Describes actions that a non-administrator user is allowed to take in
    a chat.
    """
    can_send_messages: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to send text messages,
    contacts, invoices, locations and venues"""
    can_send_audios: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to send audios"""
    can_send_documents: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to send documents"""
    can_send_photos: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to send photos"""
    can_send_videos: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to send videos"""
    can_send_video_notes: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to send video notes"""
    can_send_voice_notes: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to send voice notes"""
    can_send_polls: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to send polls"""
    can_send_other_messages: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to send animations, games,
    stickers and use inline bots"""
    can_add_web_page_previews: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to add web page previews to
    their messages"""
    can_change_info: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to change the chat title, photo
    and other settings. Ignored in public supergroups"""
    can_invite_users: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to invite new users to the chat"""
    can_pin_messages: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to pin messages. Ignored in
    public supergroups"""
    can_manage_topics: Optional[bool] = field(default=None)
    """Optional. True, if the user is allowed to create forum topics. If
    omitted defaults to the value of can_pin_messages"""




class ChatLocation(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Represents a location to which a chat is connected.
    """
    location: Location = field()
    """The location to which the supergroup is connected. Can't be a live
    location."""
    address: str = field()
    """Location address; 1-64 characters, as defined by the chat owner"""




class ForumTopic(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a forum topic.
    """
    message_thread_id: int = field()
    """Unique identifier of the forum topic"""
    name: str = field()
    """Name of the topic"""
    icon_color: int = field()
    """Color of the topic icon in RGB format"""
    icon_custom_emoji_id: Optional[str] = field(default=None)
    """Optional. Unique identifier of the custom emoji shown as the topic
    icon"""




class BotCommand(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a bot command.
    """
    command: str = field()
    """Text of the command; 1-32 characters. Can contain only lowercase
    English letters, digits and underscores."""
    description: str = field()
    """Description of the command; 1-256 characters."""




class BotCommandScope(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents the scope to which bot commands are applied.
    Currently, the following 7 scopes are supported:
    """
    ...





class BotCommandScopeDefault(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="default",
    tag_field="type"
):
    """
    Represents the default [scope](#botcommandscope) of bot commands.
    Default commands are used if no commands with a [narrower
    scope](#determining-list-of-commands) are specified for the user.
    """
    ...





class BotCommandScopeAllPrivateChats(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="all_private_chats",
    tag_field="type"
):
    """
    Represents the [scope](#botcommandscope) of bot commands, covering all
    private chats.
    """
    ...





class BotCommandScopeAllGroupChats(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="all_group_chats",
    tag_field="type"
):
    """
    Represents the [scope](#botcommandscope) of bot commands, covering all
    group and supergroup chats.
    """
    ...





class BotCommandScopeAllChatAdministrators(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="all_chat_administrators",
    tag_field="type"
):
    """
    Represents the [scope](#botcommandscope) of bot commands, covering all
    group and supergroup chat administrators.
    """
    ...





class BotCommandScopeChat(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="chat",
    tag_field="type"
):
    """
    Represents the [scope](#botcommandscope) of bot commands, covering a
    specific chat.
    """
    chat_id: Union[int, str] = field()
    """Unique identifier for the target chat or username of the target
    supergroup (in the format @supergroupusername)"""




class BotCommandScopeChatAdministrators(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="chat_administrators",
    tag_field="type"
):
    """
    Represents the [scope](#botcommandscope) of bot commands, covering all
    administrators of a specific group or supergroup chat.
    """
    chat_id: Union[int, str] = field()
    """Unique identifier for the target chat or username of the target
    supergroup (in the format @supergroupusername)"""




class BotCommandScopeChatMember(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="chat_member",
    tag_field="type"
):
    """
    Represents the [scope](#botcommandscope) of bot commands, covering a
    specific member of a group or supergroup chat.
    """
    chat_id: Union[int, str] = field()
    """Unique identifier for the target chat or username of the target
    supergroup (in the format @supergroupusername)"""
    user_id: int = field()
    """Unique identifier of the target user"""




class BotName(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents the bot's name.
    """
    name: str = field()
    """The bot's name"""




class BotDescription(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents the bot's description.
    """
    description: str = field()
    """The bot's description"""




class BotShortDescription(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents the bot's short description.
    """
    short_description: str = field()
    """The bot's short description"""




class MenuButton(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object describes the bot's menu button in a private chat. It
    should be one of
    
    If a menu button other than [MenuButtonDefault](#menubuttondefault) is
    set for a private chat, then it is applied in the chat. Otherwise the
    default menu button is applied. By default, the menu button opens the
    list of bot commands.
    """
    ...





class MenuButtonCommands(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="commands",
    tag_field="type"
):
    """
    Represents a menu button, which opens the bot's list of commands.
    """
    ...





class MenuButtonWebApp(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="web_app",
    tag_field="type"
):
    """
    Represents a menu button, which launches a [Web App](/bots/webapps).
    """
    text: str = field()
    """Text on the button"""
    web_app: WebAppInfo = field()
    """Description of the Web App that will be launched when the user presses
    the button. The Web App will be able to send an arbitrary message on
    behalf of the user using the method answerWebAppQuery."""




class MenuButtonDefault(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="default",
    tag_field="type"
):
    """
    Describes that no specific value for the menu button was set.
    """
    ...





class ResponseParameters(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Describes why a request was unsuccessful.
    """
    migrate_to_chat_id: Optional[int] = field(default=None)
    """Optional. The group has been migrated to a supergroup with the
    specified identifier. This number may have more than 32 significant
    bits and some programming languages may have difficulty/silent defects
    in interpreting it. But it has at most 52 significant bits, so a
    signed 64-bit integer or double-precision float type are safe for
    storing this identifier."""
    retry_after: Optional[int] = field(default=None)
    """Optional. In case of exceeding flood control, the number of seconds
    left to wait before the request can be repeated"""




class InputMedia(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents the content of a media message to be sent. It
    should be one of
    """
    ...





class InputMediaPhoto(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="photo",
    tag_field="type"
):
    """
    Represents a photo to be sent.
    """
    media: str = field()
    """File to send. Pass a file_id to send a file that exists on the
    Telegram servers (recommended), pass an HTTP URL for Telegram to get a
    file from the Internet, or pass “attach://<file_attach_name>” to
    upload a new one using multipart/form-data under <file_attach_name>
    name. More information on Sending Files »"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the photo to be sent, 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the photo caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    has_spoiler: Optional[bool] = field(default=None)
    """Optional. Pass True if the photo needs to be covered with a spoiler
    animation"""




class InputMediaVideo(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="video",
    tag_field="type"
):
    """
    Represents a video to be sent.
    """
    media: str = field()
    """File to send. Pass a file_id to send a file that exists on the
    Telegram servers (recommended), pass an HTTP URL for Telegram to get a
    file from the Internet, or pass “attach://<file_attach_name>” to
    upload a new one using multipart/form-data under <file_attach_name>
    name. More information on Sending Files »"""
    thumbnail: Union[InputFile, str, None] = field(default=None)
    """Optional. Thumbnail of the file sent; can be ignored if thumbnail
    generation for the file is supported server-side. The thumbnail should
    be in JPEG format and less than 200 kB in size. A thumbnail's width
    and height should not exceed 320. Ignored if the file is not uploaded
    using multipart/form-data. Thumbnails can't be reused and can be only
    uploaded as a new file, so you can pass “attach://<file_attach_name>”
    if the thumbnail was uploaded using multipart/form-data under
    <file_attach_name>. More information on Sending Files »"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the video to be sent, 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the video caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    width: Optional[int] = field(default=None)
    """Optional. Video width"""
    height: Optional[int] = field(default=None)
    """Optional. Video height"""
    duration: Optional[int] = field(default=None)
    """Optional. Video duration in seconds"""
    supports_streaming: Optional[bool] = field(default=None)
    """Optional. Pass True if the uploaded video is suitable for streaming"""
    has_spoiler: Optional[bool] = field(default=None)
    """Optional. Pass True if the video needs to be covered with a spoiler
    animation"""




class InputMediaAnimation(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="animation",
    tag_field="type"
):
    """
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without
    sound) to be sent.
    """
    media: str = field()
    """File to send. Pass a file_id to send a file that exists on the
    Telegram servers (recommended), pass an HTTP URL for Telegram to get a
    file from the Internet, or pass “attach://<file_attach_name>” to
    upload a new one using multipart/form-data under <file_attach_name>
    name. More information on Sending Files »"""
    thumbnail: Union[InputFile, str, None] = field(default=None)
    """Optional. Thumbnail of the file sent; can be ignored if thumbnail
    generation for the file is supported server-side. The thumbnail should
    be in JPEG format and less than 200 kB in size. A thumbnail's width
    and height should not exceed 320. Ignored if the file is not uploaded
    using multipart/form-data. Thumbnails can't be reused and can be only
    uploaded as a new file, so you can pass “attach://<file_attach_name>”
    if the thumbnail was uploaded using multipart/form-data under
    <file_attach_name>. More information on Sending Files »"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the animation to be sent, 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the animation caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    width: Optional[int] = field(default=None)
    """Optional. Animation width"""
    height: Optional[int] = field(default=None)
    """Optional. Animation height"""
    duration: Optional[int] = field(default=None)
    """Optional. Animation duration in seconds"""
    has_spoiler: Optional[bool] = field(default=None)
    """Optional. Pass True if the animation needs to be covered with a
    spoiler animation"""




class InputMediaAudio(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="audio",
    tag_field="type"
):
    """
    Represents an audio file to be treated as music to be sent.
    """
    media: str = field()
    """File to send. Pass a file_id to send a file that exists on the
    Telegram servers (recommended), pass an HTTP URL for Telegram to get a
    file from the Internet, or pass “attach://<file_attach_name>” to
    upload a new one using multipart/form-data under <file_attach_name>
    name. More information on Sending Files »"""
    thumbnail: Union[InputFile, str, None] = field(default=None)
    """Optional. Thumbnail of the file sent; can be ignored if thumbnail
    generation for the file is supported server-side. The thumbnail should
    be in JPEG format and less than 200 kB in size. A thumbnail's width
    and height should not exceed 320. Ignored if the file is not uploaded
    using multipart/form-data. Thumbnails can't be reused and can be only
    uploaded as a new file, so you can pass “attach://<file_attach_name>”
    if the thumbnail was uploaded using multipart/form-data under
    <file_attach_name>. More information on Sending Files »"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the audio to be sent, 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the audio caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    duration: Optional[int] = field(default=None)
    """Optional. Duration of the audio in seconds"""
    performer: Optional[str] = field(default=None)
    """Optional. Performer of the audio"""
    title: Optional[str] = field(default=None)
    """Optional. Title of the audio"""




class InputMediaDocument(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="document",
    tag_field="type"
):
    """
    Represents a general file to be sent.
    """
    media: str = field()
    """File to send. Pass a file_id to send a file that exists on the
    Telegram servers (recommended), pass an HTTP URL for Telegram to get a
    file from the Internet, or pass “attach://<file_attach_name>” to
    upload a new one using multipart/form-data under <file_attach_name>
    name. More information on Sending Files »"""
    thumbnail: Union[InputFile, str, None] = field(default=None)
    """Optional. Thumbnail of the file sent; can be ignored if thumbnail
    generation for the file is supported server-side. The thumbnail should
    be in JPEG format and less than 200 kB in size. A thumbnail's width
    and height should not exceed 320. Ignored if the file is not uploaded
    using multipart/form-data. Thumbnails can't be reused and can be only
    uploaded as a new file, so you can pass “attach://<file_attach_name>”
    if the thumbnail was uploaded using multipart/form-data under
    <file_attach_name>. More information on Sending Files »"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the document to be sent, 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the document caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    disable_content_type_detection: Optional[bool] = field(default=None)
    """Optional. Disables automatic server-side content type detection for
    files uploaded using multipart/form-data. Always True, if the document
    is sent as part of an album."""




class InputFile(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents the contents of a file to be uploaded. Must be
    posted using multipart/form-data in the usual way that files are
    uploaded via the browser.
    """
    ...





class Sticker(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a sticker.
    """
    file_id: str = field()
    """Identifier for this file, which can be used to download or reuse the
    file"""
    file_unique_id: str = field()
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots. Can't be used to download or reuse the
    file."""
    type: str = field()
    """Type of the sticker, currently one of “regular”, “mask”,
    “custom_emoji”. The type of the sticker is independent from its
    format, which is determined by the fields is_animated and is_video."""
    width: int = field()
    """Sticker width"""
    height: int = field()
    """Sticker height"""
    is_animated: bool = field()
    """True, if the sticker is animated"""
    is_video: bool = field()
    """True, if the sticker is a video sticker"""
    thumbnail: Optional[PhotoSize] = field(default=None)
    """Optional. Sticker thumbnail in the .WEBP or .JPG format"""
    emoji: Optional[str] = field(default=None)
    """Optional. Emoji associated with the sticker"""
    set_name: Optional[str] = field(default=None)
    """Optional. Name of the sticker set to which the sticker belongs"""
    premium_animation: Optional[File] = field(default=None)
    """Optional. For premium regular stickers, premium animation for the
    sticker"""
    mask_position: Optional[MaskPosition] = field(default=None)
    """Optional. For mask stickers, the position where the mask should be
    placed"""
    custom_emoji_id: Optional[str] = field(default=None)
    """Optional. For custom emoji stickers, unique identifier of the custom
    emoji"""
    needs_repainting: Optional[bool] = field(default=None)
    """Optional. True, if the sticker must be repainted to a text color in
    messages, the color of the Telegram Premium badge in emoji status,
    white color on chat photos, or another appropriate color in other
    places"""
    file_size: Optional[int] = field(default=None)
    """Optional. File size in bytes"""




class StickerSet(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a sticker set.
    """
    name: str = field()
    """Sticker set name"""
    title: str = field()
    """Sticker set title"""
    sticker_type: str = field()
    """Type of stickers in the set, currently one of “regular”, “mask”,
    “custom_emoji”"""
    is_animated: bool = field()
    """True, if the sticker set contains animated stickers"""
    is_video: bool = field()
    """True, if the sticker set contains video stickers"""
    stickers: List[Sticker] = field()
    """List of all set stickers"""
    thumbnail: Optional[PhotoSize] = field(default=None)
    """Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format"""




class MaskPosition(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object describes the position on faces where a mask should be
    placed by default.
    """
    point: str = field()
    """The part of the face relative to which the mask should be placed. One
    of “forehead”, “eyes”, “mouth”, or “chin”."""
    x_shift: float = field()
    """Shift by X-axis measured in widths of the mask scaled to the face
    size, from left to right. For example, choosing -1.0 will place mask
    just to the left of the default mask position."""
    y_shift: float = field()
    """Shift by Y-axis measured in heights of the mask scaled to the face
    size, from top to bottom. For example, 1.0 will place the mask just
    below the default mask position."""
    scale: float = field()
    """Mask scaling coefficient. For example, 2.0 means double size."""




class InputSticker(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object describes a sticker to be added to a sticker set.
    """
    sticker: Union[InputFile, str] = field()
    """The added sticker. Pass a file_id as a String to send a file that
    already exists on the Telegram servers, pass an HTTP URL as a String
    for Telegram to get a file from the Internet, upload a new one using
    multipart/form-data, or pass “attach://<file_attach_name>” to upload a
    new one using multipart/form-data under <file_attach_name> name.
    Animated and video stickers can't be uploaded via HTTP URL. More
    information on Sending Files »"""
    emoji_list: List[str] = field()
    """List of 1-20 emoji associated with the sticker"""
    mask_position: Optional[MaskPosition] = field(default=None)
    """Optional. Position where the mask should be placed on faces. For
    “mask” stickers only."""
    keywords: Optional[List[str]] = field(default=None)
    """Optional. List of 0-20 search keywords for the sticker with total
    length of up to 64 characters. For “regular” and “custom_emoji”
    stickers only."""




class InlineQuery(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents an incoming inline query. When the user sends
    an empty query, your bot could return some default or trending
    results.
    """
    id: str = field()
    """Unique identifier for this query"""
    from_: User = field(name='from')
    """Sender"""
    query: str = field()
    """Text of the query (up to 256 characters)"""
    offset: str = field()
    """Offset of the results to be returned, can be controlled by the bot"""
    chat_type: Optional[str] = field(default=None)
    """Optional. Type of the chat from which the inline query was sent. Can
    be either “sender” for a private chat with the inline query sender,
    “private”, “group”, “supergroup”, or “channel”. The chat type should
    be always known for requests sent from official clients and most
    third-party clients, unless the request was sent from a secret chat"""
    location: Optional[Location] = field(default=None)
    """Optional. Sender location, only for bots that request user location"""




class InlineQueryResultsButton(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a button to be shown above inline query
    results. You **must** use exactly one of the optional fields.
    """
    text: str = field()
    """Label text on the button"""
    web_app: Optional[WebAppInfo] = field(default=None)
    """Optional. Description of the Web App that will be launched when the
    user presses the button. The Web App will be able to switch back to
    the inline mode using the method switchInlineQuery inside the Web App."""
    start_parameter: Optional[str] = field(default=None)
    """Optional. Deep-linking parameter for the /start message sent to the
    bot when a user presses the button. 1-64 characters, only A-Z, a-z,
    0-9, _ and - are allowed.Example: An inline bot that sends YouTube
    videos can ask the user to connect the bot to their YouTube account to
    adapt search results accordingly. To do this, it displays a 'Connect
    your YouTube account' button above the results, or even before showing
    any. The user presses the button, switches to a private chat with the
    bot and, in doing so, passes a start parameter that instructs the bot
    to return an OAuth link. Once done, the bot can offer a switch_inline
    button so that the user can easily return to the chat where they
    wanted to use the bot's inline capabilities."""




class InlineQueryResult(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents one result of an inline query. Telegram clients
    currently support results of the following 20 types:
    
    **Note:** All URLs passed in inline query results will be available to
    end users and therefore must be assumed to be **public**.
    """
    ...





class InlineQueryResultArticle(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="article",
    tag_field="type"
):
    """
    Represents a link to an article or web page.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 Bytes"""
    title: str = field()
    """Title of the result"""
    input_message_content: InputMessageContent = field()
    """Content of the message to be sent"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    url: Optional[str] = field(default=None)
    """Optional. URL of the result"""
    hide_url: Optional[bool] = field(default=None)
    """Optional. Pass True if you don't want the URL to be shown in the
    message"""
    description: Optional[str] = field(default=None)
    """Optional. Short description of the result"""
    thumbnail_url: Optional[str] = field(default=None)
    """Optional. Url of the thumbnail for the result"""
    thumbnail_width: Optional[int] = field(default=None)
    """Optional. Thumbnail width"""
    thumbnail_height: Optional[int] = field(default=None)
    """Optional. Thumbnail height"""




class InlineQueryResultPhoto(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="photo",
    tag_field="type"
):
    """
    Represents a link to a photo. By default, this photo will be sent by
    the user with optional caption. Alternatively, you can use
    *input\_message\_content* to send a message with the specified content
    instead of the photo.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    photo_url: str = field()
    """A valid URL of the photo. Photo must be in JPEG format. Photo size
    must not exceed 5MB"""
    thumbnail_url: str = field()
    """URL of the thumbnail for the photo"""
    photo_width: Optional[int] = field(default=None)
    """Optional. Width of the photo"""
    photo_height: Optional[int] = field(default=None)
    """Optional. Height of the photo"""
    title: Optional[str] = field(default=None)
    """Optional. Title for the result"""
    description: Optional[str] = field(default=None)
    """Optional. Short description of the result"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the photo to be sent, 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the photo caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the photo"""




class InlineQueryResultGif(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="gif",
    tag_field="type"
):
    """
    Represents a link to an animated GIF file. By default, this animated
    GIF file will be sent by the user with optional caption.
    Alternatively, you can use *input\_message\_content* to send a message
    with the specified content instead of the animation.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    gif_url: str = field()
    """A valid URL for the GIF file. File size must not exceed 1MB"""
    thumbnail_url: str = field()
    """URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the
    result"""
    gif_width: Optional[int] = field(default=None)
    """Optional. Width of the GIF"""
    gif_height: Optional[int] = field(default=None)
    """Optional. Height of the GIF"""
    gif_duration: Optional[int] = field(default=None)
    """Optional. Duration of the GIF in seconds"""
    thumbnail_mime_type: Optional[str] = field(default=None)
    """Optional. MIME type of the thumbnail, must be one of “image/jpeg”,
    “image/gif”, or “video/mp4”. Defaults to “image/jpeg”"""
    title: Optional[str] = field(default=None)
    """Optional. Title for the result"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the GIF file to be sent, 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the caption. See formatting
    options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the GIF
    animation"""




class InlineQueryResultMpeg4Gif(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="mpeg4_gif",
    tag_field="type"
):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without
    sound). By default, this animated MPEG-4 file will be sent by the user
    with optional caption. Alternatively, you can use
    *input\_message\_content* to send a message with the specified content
    instead of the animation.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    mpeg4_url: str = field()
    """A valid URL for the MPEG4 file. File size must not exceed 1MB"""
    thumbnail_url: str = field()
    """URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the
    result"""
    mpeg4_width: Optional[int] = field(default=None)
    """Optional. Video width"""
    mpeg4_height: Optional[int] = field(default=None)
    """Optional. Video height"""
    mpeg4_duration: Optional[int] = field(default=None)
    """Optional. Video duration in seconds"""
    thumbnail_mime_type: Optional[str] = field(default=None)
    """Optional. MIME type of the thumbnail, must be one of “image/jpeg”,
    “image/gif”, or “video/mp4”. Defaults to “image/jpeg”"""
    title: Optional[str] = field(default=None)
    """Optional. Title for the result"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters
    after entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the caption. See formatting
    options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the video
    animation"""




class InlineQueryResultVideo(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="video",
    tag_field="type"
):
    """
    Represents a link to a page containing an embedded video player or a
    video file. By default, this video file will be sent by the user with
    an optional caption. Alternatively, you can use
    *input\_message\_content* to send a message with the specified content
    instead of the video.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    video_url: str = field()
    """A valid URL for the embedded video player or video file"""
    mime_type: str = field()
    """MIME type of the content of the video URL, “text/html” or “video/mp4”"""
    thumbnail_url: str = field()
    """URL of the thumbnail (JPEG only) for the video"""
    title: str = field()
    """Title for the result"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the video to be sent, 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the video caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    video_width: Optional[int] = field(default=None)
    """Optional. Video width"""
    video_height: Optional[int] = field(default=None)
    """Optional. Video height"""
    video_duration: Optional[int] = field(default=None)
    """Optional. Video duration in seconds"""
    description: Optional[str] = field(default=None)
    """Optional. Short description of the result"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the video. This
    field is required if InlineQueryResultVideo is used to send an HTML-
    page as a result (e.g., a YouTube video)."""




class InlineQueryResultAudio(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="audio",
    tag_field="type"
):
    """
    Represents a link to an MP3 audio file. By default, this audio file
    will be sent by the user. Alternatively, you can use
    *input\_message\_content* to send a message with the specified content
    instead of the audio.
    
    **Note:** This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    audio_url: str = field()
    """A valid URL for the audio file"""
    title: str = field()
    """Title"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the audio caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    performer: Optional[str] = field(default=None)
    """Optional. Performer"""
    audio_duration: Optional[int] = field(default=None)
    """Optional. Audio duration in seconds"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the audio"""




class InlineQueryResultVoice(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="voice",
    tag_field="type"
):
    """
    Represents a link to a voice recording in an .OGG container encoded
    with OPUS. By default, this voice recording will be sent by the user.
    Alternatively, you can use *input\_message\_content* to send a message
    with the specified content instead of the the voice message.
    
    **Note:** This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    voice_url: str = field()
    """A valid URL for the voice recording"""
    title: str = field()
    """Recording title"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the voice message caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    voice_duration: Optional[int] = field(default=None)
    """Optional. Recording duration in seconds"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the voice
    recording"""




class InlineQueryResultDocument(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="document",
    tag_field="type"
):
    """
    Represents a link to a file. By default, this file will be sent by the
    user with an optional caption. Alternatively, you can use
    *input\_message\_content* to send a message with the specified content
    instead of the file. Currently, only **.PDF** and **.ZIP** files can
    be sent using this method.
    
    **Note:** This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    title: str = field()
    """Title for the result"""
    document_url: str = field()
    """A valid URL for the file"""
    mime_type: str = field()
    """MIME type of the content of the file, either “application/pdf” or
    “application/zip”"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the document to be sent, 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the document caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    description: Optional[str] = field(default=None)
    """Optional. Short description of the result"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the file"""
    thumbnail_url: Optional[str] = field(default=None)
    """Optional. URL of the thumbnail (JPEG only) for the file"""
    thumbnail_width: Optional[int] = field(default=None)
    """Optional. Thumbnail width"""
    thumbnail_height: Optional[int] = field(default=None)
    """Optional. Thumbnail height"""




class InlineQueryResultLocation(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="location",
    tag_field="type"
):
    """
    Represents a location on a map. By default, the location will be sent
    by the user. Alternatively, you can use *input\_message\_content* to
    send a message with the specified content instead of the location.
    
    **Note:** This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 Bytes"""
    latitude: float = field()
    """Location latitude in degrees"""
    longitude: float = field()
    """Location longitude in degrees"""
    title: str = field()
    """Location title"""
    horizontal_accuracy: Optional[float] = field(default=None)
    """Optional. The radius of uncertainty for the location, measured in
    meters; 0-1500"""
    live_period: Optional[int] = field(default=None)
    """Optional. Period in seconds for which the location can be updated,
    should be between 60 and 86400."""
    heading: Optional[int] = field(default=None)
    """Optional. For live locations, a direction in which the user is moving,
    in degrees. Must be between 1 and 360 if specified."""
    proximity_alert_radius: Optional[int] = field(default=None)
    """Optional. For live locations, a maximum distance for proximity alerts
    about approaching another chat member, in meters. Must be between 1
    and 100000 if specified."""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the location"""
    thumbnail_url: Optional[str] = field(default=None)
    """Optional. Url of the thumbnail for the result"""
    thumbnail_width: Optional[int] = field(default=None)
    """Optional. Thumbnail width"""
    thumbnail_height: Optional[int] = field(default=None)
    """Optional. Thumbnail height"""




class InlineQueryResultVenue(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="venue",
    tag_field="type"
):
    """
    Represents a venue. By default, the venue will be sent by the user.
    Alternatively, you can use *input\_message\_content* to send a message
    with the specified content instead of the venue.
    
    **Note:** This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 Bytes"""
    latitude: float = field()
    """Latitude of the venue location in degrees"""
    longitude: float = field()
    """Longitude of the venue location in degrees"""
    title: str = field()
    """Title of the venue"""
    address: str = field()
    """Address of the venue"""
    foursquare_id: Optional[str] = field(default=None)
    """Optional. Foursquare identifier of the venue if known"""
    foursquare_type: Optional[str] = field(default=None)
    """Optional. Foursquare type of the venue, if known. (For example,
    “arts_entertainment/default”, “arts_entertainment/aquarium” or
    “food/icecream”.)"""
    google_place_id: Optional[str] = field(default=None)
    """Optional. Google Places identifier of the venue"""
    google_place_type: Optional[str] = field(default=None)
    """Optional. Google Places type of the venue. (See supported types.)"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the venue"""
    thumbnail_url: Optional[str] = field(default=None)
    """Optional. Url of the thumbnail for the result"""
    thumbnail_width: Optional[int] = field(default=None)
    """Optional. Thumbnail width"""
    thumbnail_height: Optional[int] = field(default=None)
    """Optional. Thumbnail height"""




class InlineQueryResultContact(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="contact",
    tag_field="type"
):
    """
    Represents a contact with a phone number. By default, this contact
    will be sent by the user. Alternatively, you can use
    *input\_message\_content* to send a message with the specified content
    instead of the contact.
    
    **Note:** This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 Bytes"""
    phone_number: str = field()
    """Contact's phone number"""
    first_name: str = field()
    """Contact's first name"""
    last_name: Optional[str] = field(default=None)
    """Optional. Contact's last name"""
    vcard: Optional[str] = field(default=None)
    """Optional. Additional data about the contact in the form of a vCard,
    0-2048 bytes"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the contact"""
    thumbnail_url: Optional[str] = field(default=None)
    """Optional. Url of the thumbnail for the result"""
    thumbnail_width: Optional[int] = field(default=None)
    """Optional. Thumbnail width"""
    thumbnail_height: Optional[int] = field(default=None)
    """Optional. Thumbnail height"""




class InlineQueryResultGame(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="game",
    tag_field="type"
):
    """
    Represents a [Game](#games).
    
    **Note:** This will only work in Telegram versions released after
    October 1, 2016. Older clients will not display any inline results if
    a game result is among them.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    game_short_name: str = field()
    """Short name of the game"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""




class InlineQueryResultCachedPhoto(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="photo",
    tag_field="type"
):
    """
    Represents a link to a photo stored on the Telegram servers. By
    default, this photo will be sent by the user with an optional caption.
    Alternatively, you can use *input\_message\_content* to send a message
    with the specified content instead of the photo.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    photo_file_id: str = field()
    """A valid file identifier of the photo"""
    title: Optional[str] = field(default=None)
    """Optional. Title for the result"""
    description: Optional[str] = field(default=None)
    """Optional. Short description of the result"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the photo to be sent, 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the photo caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the photo"""




class InlineQueryResultCachedGif(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="gif",
    tag_field="type"
):
    """
    Represents a link to an animated GIF file stored on the Telegram
    servers. By default, this animated GIF file will be sent by the user
    with an optional caption. Alternatively, you can use
    *input\_message\_content* to send a message with specified content
    instead of the animation.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    gif_file_id: str = field()
    """A valid file identifier for the GIF file"""
    title: Optional[str] = field(default=None)
    """Optional. Title for the result"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the GIF file to be sent, 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the caption. See formatting
    options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the GIF
    animation"""




class InlineQueryResultCachedMpeg4Gif(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="mpeg4_gif",
    tag_field="type"
):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without
    sound) stored on the Telegram servers. By default, this animated
    MPEG-4 file will be sent by the user with an optional caption.
    Alternatively, you can use *input\_message\_content* to send a message
    with the specified content instead of the animation.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    mpeg4_file_id: str = field()
    """A valid file identifier for the MPEG4 file"""
    title: Optional[str] = field(default=None)
    """Optional. Title for the result"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters
    after entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the caption. See formatting
    options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the video
    animation"""




class InlineQueryResultCachedSticker(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="sticker",
    tag_field="type"
):
    """
    Represents a link to a sticker stored on the Telegram servers. By
    default, this sticker will be sent by the user. Alternatively, you can
    use *input\_message\_content* to send a message with the specified
    content instead of the sticker.
    
    **Note:** This will only work in Telegram versions released after 9
    April, 2016 for static stickers and after 06 July, 2019 for [animated
    stickers](https://telegram.org/blog/animated-stickers). Older clients
    will ignore them.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    sticker_file_id: str = field()
    """A valid file identifier of the sticker"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the sticker"""




class InlineQueryResultCachedDocument(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="document",
    tag_field="type"
):
    """
    Represents a link to a file stored on the Telegram servers. By
    default, this file will be sent by the user with an optional caption.
    Alternatively, you can use *input\_message\_content* to send a message
    with the specified content instead of the file.
    
    **Note:** This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    title: str = field()
    """Title for the result"""
    document_file_id: str = field()
    """A valid file identifier for the file"""
    description: Optional[str] = field(default=None)
    """Optional. Short description of the result"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the document to be sent, 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the document caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the file"""




class InlineQueryResultCachedVideo(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="video",
    tag_field="type"
):
    """
    Represents a link to a video file stored on the Telegram servers. By
    default, this video file will be sent by the user with an optional
    caption. Alternatively, you can use *input\_message\_content* to send
    a message with the specified content instead of the video.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    video_file_id: str = field()
    """A valid file identifier for the video file"""
    title: str = field()
    """Title for the result"""
    description: Optional[str] = field(default=None)
    """Optional. Short description of the result"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption of the video to be sent, 0-1024 characters after
    entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the video caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the video"""




class InlineQueryResultCachedVoice(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="voice",
    tag_field="type"
):
    """
    Represents a link to a voice message stored on the Telegram servers.
    By default, this voice message will be sent by the user.
    Alternatively, you can use *input\_message\_content* to send a message
    with the specified content instead of the voice message.
    
    **Note:** This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    voice_file_id: str = field()
    """A valid file identifier for the voice message"""
    title: str = field()
    """Voice message title"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the voice message caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the voice
    message"""




class InlineQueryResultCachedAudio(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="audio",
    tag_field="type"
):
    """
    Represents a link to an MP3 audio file stored on the Telegram servers.
    By default, this audio file will be sent by the user. Alternatively,
    you can use *input\_message\_content* to send a message with the
    specified content instead of the audio.
    
    **Note:** This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.
    """
    id: str = field()
    """Unique identifier for this result, 1-64 bytes"""
    audio_file_id: str = field()
    """A valid file identifier for the audio file"""
    caption: Optional[str] = field(default=None)
    """Optional. Caption, 0-1024 characters after entities parsing"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the audio caption. See
    formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in the caption, which
    can be specified instead of parse_mode"""
    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None)
    """Optional. Inline keyboard attached to the message"""
    input_message_content: Optional[InputMessageContent] = field(default=None)
    """Optional. Content of the message to be sent instead of the audio"""




class InputMessageContent(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents the content of a message to be sent as a result
    of an inline query. Telegram clients currently support the following 5
    types:
    """
    ...





class InputTextMessageContent(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Represents the [content](#inputmessagecontent) of a text message to be
    sent as the result of an inline query.
    """
    message_text: str = field()
    """Text of the message to be sent, 1-4096 characters"""
    parse_mode: Optional[str] = field(default=None)
    """Optional. Mode for parsing entities in the message text. See
    formatting options for more details."""
    entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. List of special entities that appear in message text, which
    can be specified instead of parse_mode"""
    disable_web_page_preview: Optional[bool] = field(default=None)
    """Optional. Disables link previews for links in the sent message"""




class InputLocationMessageContent(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Represents the [content](#inputmessagecontent) of a location message
    to be sent as the result of an inline query.
    """
    latitude: float = field()
    """Latitude of the location in degrees"""
    longitude: float = field()
    """Longitude of the location in degrees"""
    horizontal_accuracy: Optional[float] = field(default=None)
    """Optional. The radius of uncertainty for the location, measured in
    meters; 0-1500"""
    live_period: Optional[int] = field(default=None)
    """Optional. Period in seconds for which the location can be updated,
    should be between 60 and 86400."""
    heading: Optional[int] = field(default=None)
    """Optional. For live locations, a direction in which the user is moving,
    in degrees. Must be between 1 and 360 if specified."""
    proximity_alert_radius: Optional[int] = field(default=None)
    """Optional. For live locations, a maximum distance for proximity alerts
    about approaching another chat member, in meters. Must be between 1
    and 100000 if specified."""




class InputVenueMessageContent(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Represents the [content](#inputmessagecontent) of a venue message to
    be sent as the result of an inline query.
    """
    latitude: float = field()
    """Latitude of the venue in degrees"""
    longitude: float = field()
    """Longitude of the venue in degrees"""
    title: str = field()
    """Name of the venue"""
    address: str = field()
    """Address of the venue"""
    foursquare_id: Optional[str] = field(default=None)
    """Optional. Foursquare identifier of the venue, if known"""
    foursquare_type: Optional[str] = field(default=None)
    """Optional. Foursquare type of the venue, if known. (For example,
    “arts_entertainment/default”, “arts_entertainment/aquarium” or
    “food/icecream”.)"""
    google_place_id: Optional[str] = field(default=None)
    """Optional. Google Places identifier of the venue"""
    google_place_type: Optional[str] = field(default=None)
    """Optional. Google Places type of the venue. (See supported types.)"""




class InputContactMessageContent(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Represents the [content](#inputmessagecontent) of a contact message to
    be sent as the result of an inline query.
    """
    phone_number: str = field()
    """Contact's phone number"""
    first_name: str = field()
    """Contact's first name"""
    last_name: Optional[str] = field(default=None)
    """Optional. Contact's last name"""
    vcard: Optional[str] = field(default=None)
    """Optional. Additional data about the contact in the form of a vCard,
    0-2048 bytes"""




class InputInvoiceMessageContent(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Represents the [content](#inputmessagecontent) of an invoice message
    to be sent as the result of an inline query.
    """
    title: str = field()
    """Product name, 1-32 characters"""
    description: str = field()
    """Product description, 1-255 characters"""
    payload: str = field()
    """Bot-defined invoice payload, 1-128 bytes. This will not be displayed
    to the user, use for your internal processes."""
    provider_token: str = field()
    """Payment provider token, obtained via @BotFather"""
    currency: str = field()
    """Three-letter ISO 4217 currency code, see more on currencies"""
    prices: List[LabeledPrice] = field()
    """Price breakdown, a JSON-serialized list of components (e.g. product
    price, tax, discount, delivery cost, delivery tax, bonus, etc.)"""
    max_tip_amount: Optional[int] = field(default=None)
    """Optional. The maximum accepted amount for tips in the smallest units
    of the currency (integer, not float/double). For example, for a
    maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp
    parameter in currencies.json, it shows the number of digits past the
    decimal point for each currency (2 for the majority of currencies).
    Defaults to 0"""
    suggested_tip_amounts: Optional[List[int]] = field(default=None)
    """Optional. A JSON-serialized array of suggested amounts of tip in the
    smallest units of the currency (integer, not float/double). At most 4
    suggested tip amounts can be specified. The suggested tip amounts must
    be positive, passed in a strictly increased order and must not exceed
    max_tip_amount."""
    provider_data: Optional[str] = field(default=None)
    """Optional. A JSON-serialized object for data about the invoice, which
    will be shared with the payment provider. A detailed description of
    the required fields should be provided by the payment provider."""
    photo_url: Optional[str] = field(default=None)
    """Optional. URL of the product photo for the invoice. Can be a photo of
    the goods or a marketing image for a service."""
    photo_size: Optional[int] = field(default=None)
    """Optional. Photo size in bytes"""
    photo_width: Optional[int] = field(default=None)
    """Optional. Photo width"""
    photo_height: Optional[int] = field(default=None)
    """Optional. Photo height"""
    need_name: Optional[bool] = field(default=None)
    """Optional. Pass True if you require the user's full name to complete
    the order"""
    need_phone_number: Optional[bool] = field(default=None)
    """Optional. Pass True if you require the user's phone number to complete
    the order"""
    need_email: Optional[bool] = field(default=None)
    """Optional. Pass True if you require the user's email address to
    complete the order"""
    need_shipping_address: Optional[bool] = field(default=None)
    """Optional. Pass True if you require the user's shipping address to
    complete the order"""
    send_phone_number_to_provider: Optional[bool] = field(default=None)
    """Optional. Pass True if the user's phone number should be sent to
    provider"""
    send_email_to_provider: Optional[bool] = field(default=None)
    """Optional. Pass True if the user's email address should be sent to
    provider"""
    is_flexible: Optional[bool] = field(default=None)
    """Optional. Pass True if the final price depends on the shipping method"""




class ChosenInlineResult(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Represents a [result](#inlinequeryresult) of an inline query that was
    chosen by the user and sent to their chat partner.
    
    **Note:** It is necessary to enable [inline
    feedback](/bots/inline#collecting-feedback) via
    [@BotFather](https://t.me/botfather) in order to receive these objects
    in updates.
    """
    result_id: str = field()
    """The unique identifier for the result that was chosen"""
    from_: User = field(name='from')
    """The user that chose the result"""
    query: str = field()
    """The query that was used to obtain the result"""
    location: Optional[Location] = field(default=None)
    """Optional. Sender location, only for bots that require user location"""
    inline_message_id: Optional[str] = field(default=None)
    """Optional. Identifier of the sent inline message. Available only if
    there is an inline keyboard attached to the message. Will be also
    received in callback queries and can be used to edit the message."""




class SentWebAppMessage(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Describes an inline message sent by a [Web App](/bots/webapps) on
    behalf of a user.
    """
    inline_message_id: Optional[str] = field(default=None)
    """Optional. Identifier of the sent inline message. Available only if
    there is an inline keyboard attached to the message."""




class LabeledPrice(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a portion of the price for goods or services.
    """
    label: str = field()
    """Portion label"""
    amount: int = field()
    """Price of the product in the smallest units of the currency (integer,
    not float/double). For example, for a price of US$ 1.45 pass amount =
    145. See the exp parameter in currencies.json, it shows the number of
    digits past the decimal point for each currency (2 for the majority of
    currencies)."""




class Invoice(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object contains basic information about an invoice.
    """
    title: str = field()
    """Product name"""
    description: str = field()
    """Product description"""
    start_parameter: str = field()
    """Unique bot deep-linking parameter that can be used to generate this
    invoice"""
    currency: str = field()
    """Three-letter ISO 4217 currency code"""
    total_amount: int = field()
    """Total price in the smallest units of the currency (integer, not
    float/double). For example, for a price of US$ 1.45 pass amount = 145.
    See the exp parameter in currencies.json, it shows the number of
    digits past the decimal point for each currency (2 for the majority of
    currencies)."""




class ShippingAddress(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a shipping address.
    """
    country_code: str = field()
    """Two-letter ISO 3166-1 alpha-2 country code"""
    state: str = field()
    """State, if applicable"""
    city: str = field()
    """City"""
    street_line1: str = field()
    """First line for the address"""
    street_line2: str = field()
    """Second line for the address"""
    post_code: str = field()
    """Address post code"""




class OrderInfo(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents information about an order.
    """
    name: Optional[str] = field(default=None)
    """Optional. User name"""
    phone_number: Optional[str] = field(default=None)
    """Optional. User's phone number"""
    email: Optional[str] = field(default=None)
    """Optional. User email"""
    shipping_address: Optional[ShippingAddress] = field(default=None)
    """Optional. User shipping address"""




class ShippingOption(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents one shipping option.
    """
    id: str = field()
    """Shipping option identifier"""
    title: str = field()
    """Option title"""
    prices: List[LabeledPrice] = field()
    """List of price portions"""




class SuccessfulPayment(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object contains basic information about a successful payment.
    """
    currency: str = field()
    """Three-letter ISO 4217 currency code"""
    total_amount: int = field()
    """Total price in the smallest units of the currency (integer, not
    float/double). For example, for a price of US$ 1.45 pass amount = 145.
    See the exp parameter in currencies.json, it shows the number of
    digits past the decimal point for each currency (2 for the majority of
    currencies)."""
    invoice_payload: str = field()
    """Bot specified invoice payload"""
    telegram_payment_charge_id: str = field()
    """Telegram payment identifier"""
    provider_payment_charge_id: str = field()
    """Provider payment identifier"""
    shipping_option_id: Optional[str] = field(default=None)
    """Optional. Identifier of the shipping option chosen by the user"""
    order_info: Optional[OrderInfo] = field(default=None)
    """Optional. Order information provided by the user"""




class ShippingQuery(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object contains information about an incoming shipping query.
    """
    id: str = field()
    """Unique query identifier"""
    from_: User = field(name='from')
    """User who sent the query"""
    invoice_payload: str = field()
    """Bot specified invoice payload"""
    shipping_address: ShippingAddress = field()
    """User specified shipping address"""




class PreCheckoutQuery(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object contains information about an incoming pre-checkout query.
    """
    id: str = field()
    """Unique query identifier"""
    from_: User = field(name='from')
    """User who sent the query"""
    currency: str = field()
    """Three-letter ISO 4217 currency code"""
    total_amount: int = field()
    """Total price in the smallest units of the currency (integer, not
    float/double). For example, for a price of US$ 1.45 pass amount = 145.
    See the exp parameter in currencies.json, it shows the number of
    digits past the decimal point for each currency (2 for the majority of
    currencies)."""
    invoice_payload: str = field()
    """Bot specified invoice payload"""
    shipping_option_id: Optional[str] = field(default=None)
    """Optional. Identifier of the shipping option chosen by the user"""
    order_info: Optional[OrderInfo] = field(default=None)
    """Optional. Order information provided by the user"""




class PassportData(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Describes Telegram Passport data shared with the bot by the user.
    """
    data: List[EncryptedPassportElement] = field()
    """Array with information about documents and other Telegram Passport
    elements that was shared with the bot"""
    credentials: EncryptedCredentials = field()
    """Encrypted credentials required to decrypt the data"""




class PassportFile(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a file uploaded to Telegram Passport. Currently
    all Telegram Passport files are in JPEG format when decrypted and
    don't exceed 10MB.
    """
    file_id: str = field()
    """Identifier for this file, which can be used to download or reuse the
    file"""
    file_unique_id: str = field()
    """Unique identifier for this file, which is supposed to be the same over
    time and for different bots. Can't be used to download or reuse the
    file."""
    file_size: int = field()
    """File size in bytes"""
    file_date: int = field()
    """Unix time when the file was uploaded"""




class EncryptedPassportElement(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Describes documents or other Telegram Passport elements shared with
    the bot by the user.
    """
    type: str = field()
    """Element type. One of “personal_details”, “passport”, “driver_license”,
    “identity_card”, “internal_passport”, “address”, “utility_bill”,
    “bank_statement”, “rental_agreement”, “passport_registration”,
    “temporary_registration”, “phone_number”, “email”."""
    hash: str = field()
    """Base64-encoded element hash for using in
    PassportElementErrorUnspecified"""
    data: Optional[str] = field(default=None)
    """Optional. Base64-encoded encrypted Telegram Passport element data
    provided by the user, available for “personal_details”, “passport”,
    “driver_license”, “identity_card”, “internal_passport” and “address”
    types. Can be decrypted and verified using the accompanying
    EncryptedCredentials."""
    phone_number: Optional[str] = field(default=None)
    """Optional. User's verified phone number, available only for
    “phone_number” type"""
    email: Optional[str] = field(default=None)
    """Optional. User's verified email address, available only for “email”
    type"""
    files: Optional[List[PassportFile]] = field(default=None)
    """Optional. Array of encrypted files with documents provided by the
    user, available for “utility_bill”, “bank_statement”,
    “rental_agreement”, “passport_registration” and
    “temporary_registration” types. Files can be decrypted and verified
    using the accompanying EncryptedCredentials."""
    front_side: Optional[PassportFile] = field(default=None)
    """Optional. Encrypted file with the front side of the document, provided
    by the user. Available for “passport”, “driver_license”,
    “identity_card” and “internal_passport”. The file can be decrypted and
    verified using the accompanying EncryptedCredentials."""
    reverse_side: Optional[PassportFile] = field(default=None)
    """Optional. Encrypted file with the reverse side of the document,
    provided by the user. Available for “driver_license” and
    “identity_card”. The file can be decrypted and verified using the
    accompanying EncryptedCredentials."""
    selfie: Optional[PassportFile] = field(default=None)
    """Optional. Encrypted file with the selfie of the user holding a
    document, provided by the user; available for “passport”,
    “driver_license”, “identity_card” and “internal_passport”. The file
    can be decrypted and verified using the accompanying
    EncryptedCredentials."""
    translation: Optional[List[PassportFile]] = field(default=None)
    """Optional. Array of encrypted files with translated versions of
    documents provided by the user. Available if requested for “passport”,
    “driver_license”, “identity_card”, “internal_passport”,
    “utility_bill”, “bank_statement”, “rental_agreement”,
    “passport_registration” and “temporary_registration” types. Files can
    be decrypted and verified using the accompanying EncryptedCredentials."""




class EncryptedCredentials(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    Describes data required for decrypting and authenticating
    [EncryptedPassportElement](#encryptedpassportelement). See the
    [Telegram Passport Documentation](/passport#receiving-information) for
    a complete description of the data decryption and authentication
    processes.
    """
    data: str = field()
    """Base64-encoded encrypted JSON-serialized data with unique user's
    payload, data hashes and secrets required for EncryptedPassportElement
    decryption and authentication"""
    hash: str = field()
    """Base64-encoded data hash for data authentication"""
    secret: str = field()
    """Base64-encoded secret, encrypted with the bot's public RSA key,
    required for data decryption"""




class PassportElementError(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents an error in the Telegram Passport element which
    was submitted that should be resolved by the user. It should be one
    of:
    """
    ...





class PassportElementErrorDataField(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="data",
    tag_field="source"
):
    """
    Represents an issue in one of the data fields that was provided by the
    user. The error is considered resolved when the field's value changes.
    """
    type: str = field()
    """The section of the user's Telegram Passport which has the error, one
    of “personal_details”, “passport”, “driver_license”, “identity_card”,
    “internal_passport”, “address”"""
    field_name: str = field()
    """Name of the data field which has the error"""
    data_hash: str = field()
    """Base64-encoded data hash"""
    message: str = field()
    """Error message"""




class PassportElementErrorFrontSide(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="front_side",
    tag_field="source"
):
    """
    Represents an issue with the front side of a document. The error is
    considered resolved when the file with the front side of the document
    changes.
    """
    type: str = field()
    """The section of the user's Telegram Passport which has the issue, one
    of “passport”, “driver_license”, “identity_card”, “internal_passport”"""
    file_hash: str = field()
    """Base64-encoded hash of the file with the front side of the document"""
    message: str = field()
    """Error message"""




class PassportElementErrorReverseSide(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="reverse_side",
    tag_field="source"
):
    """
    Represents an issue with the reverse side of a document. The error is
    considered resolved when the file with reverse side of the document
    changes.
    """
    type: str = field()
    """The section of the user's Telegram Passport which has the issue, one
    of “driver_license”, “identity_card”"""
    file_hash: str = field()
    """Base64-encoded hash of the file with the reverse side of the document"""
    message: str = field()
    """Error message"""




class PassportElementErrorSelfie(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="selfie",
    tag_field="source"
):
    """
    Represents an issue with the selfie with a document. The error is
    considered resolved when the file with the selfie changes.
    """
    type: str = field()
    """The section of the user's Telegram Passport which has the issue, one
    of “passport”, “driver_license”, “identity_card”, “internal_passport”"""
    file_hash: str = field()
    """Base64-encoded hash of the file with the selfie"""
    message: str = field()
    """Error message"""




class PassportElementErrorFile(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="file",
    tag_field="source"
):
    """
    Represents an issue with a document scan. The error is considered
    resolved when the file with the document scan changes.
    """
    type: str = field()
    """The section of the user's Telegram Passport which has the issue, one
    of “utility_bill”, “bank_statement”, “rental_agreement”,
    “passport_registration”, “temporary_registration”"""
    file_hash: str = field()
    """Base64-encoded file hash"""
    message: str = field()
    """Error message"""




class PassportElementErrorFiles(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="files",
    tag_field="source"
):
    """
    Represents an issue with a list of scans. The error is considered
    resolved when the list of files containing the scans changes.
    """
    type: str = field()
    """The section of the user's Telegram Passport which has the issue, one
    of “utility_bill”, “bank_statement”, “rental_agreement”,
    “passport_registration”, “temporary_registration”"""
    file_hashes: List[str] = field()
    """List of base64-encoded file hashes"""
    message: str = field()
    """Error message"""




class PassportElementErrorTranslationFile(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="translation_file",
    tag_field="source"
):
    """
    Represents an issue with one of the files that constitute the
    translation of a document. The error is considered resolved when the
    file changes.
    """
    type: str = field()
    """Type of element of the user's Telegram Passport which has the issue,
    one of “passport”, “driver_license”, “identity_card”,
    “internal_passport”, “utility_bill”, “bank_statement”,
    “rental_agreement”, “passport_registration”, “temporary_registration”"""
    file_hash: str = field()
    """Base64-encoded file hash"""
    message: str = field()
    """Error message"""




class PassportElementErrorTranslationFiles(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="translation_files",
    tag_field="source"
):
    """
    Represents an issue with the translated version of a document. The
    error is considered resolved when a file with the document translation
    change.
    """
    type: str = field()
    """Type of element of the user's Telegram Passport which has the issue,
    one of “passport”, “driver_license”, “identity_card”,
    “internal_passport”, “utility_bill”, “bank_statement”,
    “rental_agreement”, “passport_registration”, “temporary_registration”"""
    file_hashes: List[str] = field()
    """List of base64-encoded file hashes"""
    message: str = field()
    """Error message"""




class PassportElementErrorUnspecified(
    Schema,
    kw_only=True,
    omit_defaults=True,
    tag="unspecified",
    tag_field="source"
):
    """
    Represents an issue in an unspecified place. The error is considered
    resolved when new data is added.
    """
    type: str = field()
    """Type of element of the user's Telegram Passport which has the issue"""
    element_hash: str = field()
    """Base64-encoded element hash"""
    message: str = field()
    """Error message"""




class Game(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents a game. Use BotFather to create and edit games,
    their short names will act as unique identifiers.
    """
    title: str = field()
    """Title of the game"""
    description: str = field()
    """Description of the game"""
    photo: List[PhotoSize] = field()
    """Photo that will be displayed in the game message in chats."""
    text: Optional[str] = field(default=None)
    """Optional. Brief description of the game or high scores included in the
    game message. Can be automatically edited to include current high
    scores for the game when the bot calls setGameScore, or manually
    edited using editMessageText. 0-4096 characters."""
    text_entities: Optional[List[MessageEntity]] = field(default=None)
    """Optional. Special entities that appear in text, such as usernames,
    URLs, bot commands, etc."""
    animation: Optional[Animation] = field(default=None)
    """Optional. Animation that will be displayed in the game message in
    chats. Upload via BotFather"""




class CallbackGame(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    A placeholder, currently holds no information. Use
    [BotFather](https://t.me/botfather) to set up your game.
    """
    ...





class GameHighScore(
    Schema,
    kw_only=True,
    omit_defaults=True
):
    """
    This object represents one row of the high scores table for a game.
    
    And that's about all we've got for now.
    If you've got any questions, please check out our [**Bot FAQ
    »**](/bots/faq)
    """
    position: int = field()
    """Position in high score table for the game"""
    user: User = field()
    """User"""
    score: int = field()
    """Score"""


