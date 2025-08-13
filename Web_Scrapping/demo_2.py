import csv
import random
import time
from datetime import datetime
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright
from fake_useragent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent as RandomUA