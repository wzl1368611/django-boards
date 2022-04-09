#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2020-8-9 23:11:00
# version: 1.0
# __author__: zhilong

from django.test import TestCase
from ..forms import SignUpForm


class SignUpFormTest(TestCase):

    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username','email','password1','password2']
        actual = list(form.fields)
        self.assertSequenceEqual(expected,actual)





