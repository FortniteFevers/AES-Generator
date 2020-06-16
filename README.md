#FeversBR

FeversBR is a utility which generates the current Fortnite News Updates and shares it on Twitter with a caption of the body and title.

As seen on [@FeversBot](https://twitter.com/FeversBot/status/1270814360114540561)...

<p align="center">
    <img src="https://i.imgur.com/YXoesjJ.png" width="650px" draggable="false">
</p>

## Requirements

- [Python 3.7](https://www.python.org/downloads/)
- [Requests](http://docs.python-requests.org/en/master/user/install/)
- [colorama](https://pypi.org/project/colorama/)
- [Pillow](https://pillow.readthedocs.io/en/stable/installation.html#basic-installation)
- [python-twitter](https://github.com/bear/python-twitter#installing)

A [Fortnite-API API Key](https://fortnite-api.com/profile) is required to obtain the Item Shop data, [Twitter API credentials](https://developer.twitter.com/en/apps) are required to Tweet the image.

## Usage

Open `bot-example.py` in your preferred text editor, fill in all your API keys where it says too. Once finished, save and rename the file to `bot.py`.


FeversPY is designed to be ran using a scheduler, such as [Zcron](https://www.z-cron.com/).

```
python bot.py
```

## Credits

- Item Shop data provided by [Fortnite-API](https://fortnite-api.com/)