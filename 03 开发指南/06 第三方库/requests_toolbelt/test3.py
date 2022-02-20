"""

"""
from clint.textui.progress import Bar as ProgressBar
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

import requests


def create_callback(encoder):
    encoder_len = encoder.len
    bar = ProgressBar(expected_size=encoder_len, filled_char='=')

    def callback(monitor):
        bar.show(monitor.bytes_read)
        print(1)
    return callback


encoder = MultipartEncoder({
    'form_field': 'value',
    'another_form_field': 'another value',
    'first_file': ('node-v16.13.0-Linux-x64.tar.xz', open(__file__, 'rb'), 'text/plain'),
    'second_file': ('node-v16.13.0-Linux-x64.tar.xz', open(__file__, 'rb'),
                    'text/xz'),
})

callback = create_callback(encoder)
monitor = MultipartEncoderMonitor(encoder, callback)
r = requests.post('https://httpbin.org/post', data=monitor,
                  headers={'Content-Type': monitor.content_type})
print('\nUpload finished! (Returned status {0} {1})'.format(
    r.status_code, r.reason
))
