import datetime
import io
from typing import List, Optional

from chat_exporter.construct.transcript import Transcript
from chat_exporter.ext.discord_import import hikari


async def quick_export(
    channel: hikari.channels.PartialChannel,
    guild: Optional[hikari.guilds.Guild] = None,
    bot: Optional[hikari.GatewayBot] = None,
):
    """
    Create a quick export of your Discord channel.
    This function will produce the transcript and post it back in to your channel.
    :param channel: hikari.channels.PartialChannel
    :param guild: (optional) hikari.guilds.Guild
    :param bot: (optional) hikari.GatewayBot
    :return: hikari.messages.Message (posted transcript)
    """

    if guild:
        channel.guild = guild

    transcript = (
        await Transcript(
            channel=channel,
            limit=None,
            messages=None,
            pytz_timezone="UTC",
            military_time=True,
            fancy_times=True,
            before=hikari.undefined.UNDEFINED,
            after=hikari.undefined.UNDEFINED,
            support_dev=True,
            bot=bot,
            ).export()
        ).html

    if not transcript:
        return

    transcript_embed = hikari.embeds.Embed(
        description=f"**Transcript Name:** transcript-{channel.name}\n\n",
        color=hikari.Color(0x5865F2)
    )

    transcript_file = hikari.files.Bytes(io.BytesIO(transcript.encode()), f"transcript-{channel.name}.html")
    return await channel.send(embed=transcript_embed, attachment=transcript_file)


async def export(
    channel: hikari.channels.PartialChannel,
    limit: Optional[int] = None,
    tz_info="UTC",
    guild: Optional[hikari.guilds.Guild] = None,
    bot: Optional[hikari.GatewayBot] = None,
    military_time: Optional[bool] = True,
    fancy_times: Optional[bool] = True,
    before: hikari.undefined.UndefinedOr[hikari.snowflakes.SearchableSnowflakeishOr[hikari.snowflakes.Unique]] = hikari.undefined.UNDEFINED,
    after: hikari.undefined.UndefinedOr[hikari.snowflakes.SearchableSnowflakeishOr[hikari.snowflakes.Unique]] = hikari.undefined.UNDEFINED,
    support_dev: Optional[bool] = True,
):
    """
    Create a customised transcript of your Discord channel.
    This function will return the transcript which you can then turn in to a file to post wherever.
    :param channel: hikari.channels.PartialChannel - channel to Export
    :param limit: (optional) integer - limit of messages to capture
    :param tz_info: (optional) TZ Database Name - set the timezone of your transcript
    :param guild: (optional) hikari.guilds.Guild - solution for edpy
    :param bot: (optional) hikari.GatewayBot - set getting member role colour
    :param military_time: (optional) boolean - set military time (24hour clock)
    :param fancy_times: (optional) boolean - set javascript around time display
    :param before: (optional) datetime.datetime - allows before time for history
    :param after: (optional) datetime.datetime - allows after time for history
    :param support_dev
    :return: string - transcript file make up
    """
    if guild:
        channel.guild = guild

    return (
        await Transcript(
            channel=channel,
            limit=limit,
            messages=None,
            pytz_timezone=tz_info,
            military_time=military_time,
            fancy_times=fancy_times,
            before=before,
            after=after,
            support_dev=support_dev,
            bot=bot,
        ).export()
    ).html


async def raw_export(
    channel: hikari.channels.PartialChannel,
    messages: List[hikari.messages.Message],
    tz_info="UTC",
    guild: Optional[hikari.guilds.Guild] = None,
    bot: Optional[hikari.GatewayBot] = None,
    military_time: Optional[bool] = False,
    fancy_times: Optional[bool] = True,
    support_dev: Optional[bool] = True,
):
    """
    Create a customised transcript with your own captured Discord messages
    This function will return the transcript which you can then turn in to a file to post wherever.
    :param channel: hikari.channels.PartialChannel - channel to Export
    :param messages: List[hikari.messages.Message] - list of Discord messages to export
    :param tz_info: (optional) TZ Database Name - set the timezone of your transcript
    :param guild: (optional) hikari.guilds.Guild - solution for edpy
    :param bot: (optional) hikari.GatewayBot - set getting member role colour
    :param military_time: (optional) boolean - set military time (24hour clock)
    :param fancy_times: (optional) boolean - set javascript around time display
    :param support_dev
    :return: string - transcript file make up
    """
    if guild:
        channel.guild = guild

    return (
        await Transcript(
            channel=channel,
            limit=None,
            messages=messages,
            pytz_timezone=tz_info,
            military_time=military_time,
            fancy_times=fancy_times,
            before=hikari.undefined.UNDEFINED,
            after=hikari.undefined.UNDEFINED,
            support_dev=support_dev,
            bot=bot,
        ).export()
    ).html


async def quick_link(
    channel: hikari.channels.PartialChannel,
    message: hikari.messages.Message
):
    """
    Create a quick link for your transcript file.
    This function will return an embed with a link to view the transcript online.
    :param channel: hikari.channels.PartialChannel
    :param message: hikari.messages.Message
    :return: hikari.messages.Message (posted link)
    """
    embed = hikari.embeds.Embed(
        title="Transcript Link",
        description=(
            f"[Click here to view the transcript](https://mahto.id/chat-exporter?url={message.attachments[0].url})"
        ),
        color=hikari.Color(0x5865F2),
    )

    return await channel.send(embed=embed)


async def link(
    message: hikari.messages.Message
):
    """
    Returns a link which you can use to display in a message.
    This function will return a string of the link.
    :param message: hikari.messages.Message
    :return: string (link: https://mahto.id/chat-exporter?url=ATTACHMENT_URL)
    """
    return "https://mahto.id/chat-exporter?url=" + message.attachments[0].url
