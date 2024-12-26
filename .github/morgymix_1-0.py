import sys
from pathlib import Path
import _util


def main(args):
  _util.download_model(873021)

  _util.replace_defaults({
    'DEFAULT_VAE_NAME': None,
    'DEFAULT_POS_PREPROMPT': "score_9, score_8_up, score_7_up, ",
    'DEFAULT_NEG_PREPROMPT': "",
    'DEFAULT_POSITIVE_PROMPT': "safe",
    'DEFAULT_NEGATIVE_PROMPT': "",
    'DEFAULT_CFG': 6,
    'DEFAULT_CLIP_SKIP': 2,
    'DEFAULT_WIDTH': 832,
    'DEFAULT_HEIGHT': 1216,
    'DEFAULT_SCHEDULER': "Euler a",
    'DEFAULT_STEPS': 24
  })


if __name__ == '__main__':
  main(sys.argv[1:])
