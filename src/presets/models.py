from django.db import models


class Preset(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True, null=True)
    video = models.BooleanField(default=False)
    audio = models.BooleanField(default=False)

    # VIDEO PART
    video_codecs = (("libx264", "H264"), ("libx265", "HEVC"))
    resolutions = (("qvga", "QVGA (320x240)"),
                   ("vga", "VGA (640x480)"),
                   ("ntsc", "NTSC (720x480)"),
                   ("pal", "PAL (720x576)"),
                   ("hd480", "480P (852x480)"),
                   ("hd720", "720P (1280x720)"),
                   ("hd1080", "1080P (1920x1080)"),
                   ("2k", "2K (2048x1080)"),
                   ("4k", "4K (4096x2160)")
                   )
    video_codec = models.CharField(max_length=32, choices=video_codecs)
    video_vresolution = models.CharField(max_length=32, choices=resolutions)
    video_bitrate = models.PositiveIntegerField(null=False, default=0)
    video_framerate = models.PositiveIntegerField(null=False, default=0)
    advanced_video_encoding = models.BooleanField(default=False)
    cbr = models.BooleanField(default=False)
    video_min_bitrate = models.PositiveIntegerField(null=False)
    video_max_bitrate = models.PositiveIntegerField(null=False)
    video_presets = (("ultrafast", "Ultrafast"),
                     ("superfast", "Superfast"),
                     ("veryfast", "Veryfast"),
                     ("faster", "Faster"),
                     ("fast", "Fast"),
                     ("medium", "Medium"),
                     ("slow", "Slow"),
                     ("slower", "Slower"),
                     ("veryslow", "Veryslow")
                     )
    video_profiles = (("baseline", "Baseline"),
                      ("main", "Main"),
                      ("high", "High"),
                      ("high10", "High10"),
                      ("high422", "High422"),
                      ("high444", "High444"))
    video_preset = models.CharField(max_length=32, choices=video_presets, default="medium")
    video_profile = models.CharField(max_length=32, choices=video_profiles, default="main")
    video_buffer = models.PositiveIntegerField(null=True)
    video_gop = models.PositiveIntegerField(null=True)
    video_kyeframe_interval = models.PositiveIntegerField(null=True)
    enable_deinterlace = models.BooleanField(default=False)
    enable_zero_latency = models.BooleanField(default=False)

    # AUDIO PART
    audio_codecs = (("aac", "AAC"), ("libopus", "Libopus"))
    audio_bitrates = (("64", "64"),
                      ("96", "96"),
                      ("128", "128"),
                      ("144", "144"),
                      ("160", "160"),
                      ("192", "192"),
                      ("256", "256")
                      )
    audio_sample_rates = (("44100", "44.1 khz"),
                          ("48000", "48 khz"),
                          ("88200", "88.2 khz"),
                          ("96000", "96 khz"),
                          ("192000", "192 khz")
                          )
    audio_codec = models.CharField(max_length=32, choices=audio_codecs, default='aac')
    audio_channels = models.CharField(max_length=32, choices=(("1", "Mono"), ("2", "Stereo")), default='2')
    audio_bitrate = models.CharField(max_length=32, choices=audio_bitrates, default='144')
    audio_sample_rate = models.CharField(max_length=32, choices=audio_sample_rates, default='44100')
    advanced_audio_encoding = models.BooleanField(default=False)
    audio_gain = models.CharField(max_length=32, choices=(("-20db", "-20db"),
                                           ("-10db", "-10db"),
                                           ("0db", "0db"),
                                           ("10db", "10db"),
                                           ("20db", "20db")),
                                  default="0db")
    audio_delay = models.IntegerField(default=0)










