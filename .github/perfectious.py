import sys
from pathlib import Path
import _util


def main(args):
  _util.download_model(1111838)

  _util.replace_defaults({
    'DEFAULT_VAE_NAME': None,
    'DEFAULT_POS_PREPROMPT': "masterpiece, best quality, amazing quality, very aesthetic, absurdres,",
    'DEFAULT_NEG_PREPROMPT': "<low quality, worst quality, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry, bad feet, cropped, poorly drawn hands, poorly drawn face, mutation, deformed, extra limbs, extra arms, extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed, mutated hands, polar lowres, bad body, bad proportions, gross proportions, wrong shadows>
",
    'DEFAULT_POSITIVE_PROMPT': "",
    'DEFAULT_NEGATIVE_PROMPT': "",
    'DEFAULT_CFG': 6,
    'DEFAULT_CLIP_SKIP': 2,
    'DEFAULT_WIDTH': 1024,
    'DEFAULT_HEIGHT': 1024,
    'DEFAULT_SCHEDULER': "Euler a",
    'DEFAULT_STEPS': 25
  })


if __name__ == '__main__':
  main(sys.argv[1:])
