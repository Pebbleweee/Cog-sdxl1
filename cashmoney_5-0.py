import sys
from pathlib import Path
import _util


def main(args):
  _util.download_model(886215)

  _util.replace_defaults({
    'DEFAULT_VAE_NAME': None,
    'DEFAULT_POS_PREPROMPT': "",
    'DEFAULT_NEG_PREPROMPT': "lowres, worst quality, low quality, bad anatomy, bad hands, ",
    'DEFAULT_POSITIVE_PROMPT': "safe",
    'DEFAULT_NEGATIVE_PROMPT': "",
    'DEFAULT_CFG': 6.5,
    'DEFAULT_CLIP_SKIP': 1,
    'DEFAULT_WIDTH': 832,
    'DEFAULT_HEIGHT': 1216,
    'DEFAULT_SCHEDULER': "DPM2 a",
    'DEFAULT_STEPS': 28
  })


if __name__ == '__main__':
  main(sys.argv[1:])
