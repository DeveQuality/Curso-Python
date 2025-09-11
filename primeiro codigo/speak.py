import androidhelper # type: ignore

droid = androidhelper.Android()
message = droid.dialogGetInput('TTS', 'what would you say').result
droid.ttsSpeak(message)