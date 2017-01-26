#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

def build_page(textarea_content, error):
    header = "<h2>Web Caesar</h2>"
    message_label = "<label>Message:</label>"
    textarea = "<textarea name='message'>" + textarea_content + "</textarea>"
    rot_label = "<label>Rotation Key:</label>"
    rot_amt = "<input type='number' name='rotation_num' />"
    submit = "<input type='submit' />"
    error_msg = "<p><b>" + error + "</b></p>"
    form = ("<form method='post'>"
            + header
            + "<br>"
            + rot_label
            + rot_amt
            + "<br>"
            + "<br>"
            + message_label
            + textarea
            + "<br>"
            + submit
            + error_msg
            + "</form>")

    return form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("", "")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")  #gets the info from the message feild
        rot_num = self.request.get("rotation_num")
        if rot_num.isdigit():
            encrypted_message = caesar.encrypt(message, rot_num)
            escaped_message = cgi.escape(encrypted_message)
            content = build_page(escaped_message, "")
            self.response.write(content)
        else:
            error_txt = "You must enter a rotation key number"
            escaped_message = cgi.escape(message)    # because we haven't encrypted yet
            content = build_page(escaped_message, error_txt)
            self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
