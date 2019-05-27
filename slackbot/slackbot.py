import os
import slack


class SlackBot:
    BASE_URL = "https://www.slack.com/api/"

    def __init__(self, token=None, base_url=None, timeout=30, loop=None, ssl=None, proxy=None, run_async=False, session=None):
        self.token = token or os.environ.get('SLACK_API_TOKEN')
        if self.token is None:
            raise ValueError('Must provide slack API token. Can use environment variable "SLACK_API_TOKEN"')
        self.base_url = base_url or self.BASE_URL
        self.client = slack.WebClient(
            token=self.token,
            base_url=self.BASE_URL,
            timeout=timeout,
            loop=loop,
            ssl=ssl,
            proxy=proxy,
            run_async=run_async,
            session=session
        )

    def send_message(self, channel, message, as_user=True, **kwargs):
        return self.client.chat_postMessage(
            channel=channel,
            text=message,
            as_user=as_user,
            kwargs=kwargs
        )

    def send_file(self, channel, file, message=None, **kwargs):
        return self.client.files_upload(
            channels=channel,
            file=file,
            initial_comment=message or '',
            kwargs=kwargs
        )
