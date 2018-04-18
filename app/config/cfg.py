import configparser
import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--env', type=str, default='dev')
args = parser.parse_args()


class CrowdConfig:
    env = 'dev'

    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read("cfg.ini")

    def get(self, option):
        return self.cfg.get(CrowdConfig.env, option)

    def getint(self, option):
        return self.cfg.getint(CrowdConfig.env, option)


CrowdConfig.env = args.env
cfg = CrowdConfig()
