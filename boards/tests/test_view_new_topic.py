#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2020-8-9 23:11:00
# version: 1.0
# __author__: zhilong


from django.test import TestCase
from django.urls import reverse
from ..models import Board


class LoginRequiredNewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django',description='Django Board.')
        self.url = reverse('new_topic',kwargs={'pk':1})
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response,'{login_url}?next={url}'.format(login_url=login_url,url=self.url))





