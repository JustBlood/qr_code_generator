import qrcode
a = 1
img = qrcode.make('GitHub Webhook')
img.save("gitHub_webhook.png")