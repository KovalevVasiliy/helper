import os


class Settings:
    VK_APP_KEY: str = os.getenv('VK_APP_KEY', None)
    VK_GROUP: str = os.getenv('VK_GROUP', None)
    VK_TO_GROUP_ID: str = os.getenv('VK_TO_GROUP_ID', None)
