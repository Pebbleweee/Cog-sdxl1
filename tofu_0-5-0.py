import sys
from pathlib import Path
import _util


def main(args):
  _util.download_model(826511)

  _util.replace_defaults({
    'DEFAULT_VAE_NAME': "sdxl-vae-fp16-fix",
    'DEFAULT_POS_PREPROMPT': "masterpiece, best quality, ",
    'DEFAULT_NEG_PREPROMPT': "(worst quality, low quality:1.1), error, bad hands, watermark, distorted, ",
    'DEFAULT_POSITIVE_PROMPT': "safe",
    'DEFAULT_NEGATIVE_PROMPT': "",
    'DEFAULT_CFG': 7,
    'DEFAULT_CLIP_SKIP': 1,
    'DEFAULT_WIDTH': 832,
    'DEFAULT_HEIGHT': 1216,
    'DEFAULT_SCHEDULER': "Euler a",
    'DEFAULT_STEPS': 28
  })

  (vae_dir := Path('vaes/sdxl-vae-fp16-fix')).mkdir()

  _util.aria_dl(
    "https://huggingface.co/madebyollin/sdxl-vae-fp16-fix/resolve/main/diffusion_pytorch_model.safetensors",
    vae_dir, "diffusion_pytorch_model.safetensors"
  )
  _util.aria_dl(
    "https://huggingface.co/madebyollin/sdxl-vae-fp16-fix/resolve/main/config.json",
    vae_dir, "config.json"
  )


if __name__ == '__main__':
  main(sys.argv[1:])
