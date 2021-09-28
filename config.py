import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.environ.get("API_ID", "8634206"))
    API_HASH = os.environ.get("API_HASH", "fc8f066ba30e9cc6b0da2af1561f2744")
    LOG_ID = int(os.environ.get("LOG_ID", "0"))
    SESSION_STRING = os.environ.get("SESSION_STRING", "AgAM2GjROA6X9Cjdscn0pTJum7BdZmNZzmRw8XcGjWTVDUKTEBirCUeJCDTngEoKvQJBHyCSjKJYMpw80efiSatOXo6BWCRSKL9opGD1dk90LKFXtcVgzvMnDbJP9MkEvb7RykutSgSdBfOoGj_Z5Pvub9CuyGBB_12YB0_hKMU_zQym0iyALBWFVcQCYBQwT4TlOMm7JCMwQ1Yt34Xz66ksbl_o7gcaZJe6o5FePUlBsE4tMwQ-FlKSXXVO-ZGTmZeSSPDtqqn2e_KUoRLfjII9R9elcpkCE76JcNL3eH75VdFm0mVoY6PtvDLWZ7Eii8mDj2MxH1t2dZtO5lFGqgd7d6VUsQA")

class Database:
    VIDEO_CALL = {}
    RADIO_CALL = {}
    FFMPEG_PROCESSES = {}
