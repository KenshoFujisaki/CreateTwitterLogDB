#!/usr/bin/python
# coding: UTF-8

import csv
import sys
import codecs
import re

# 文字コーディング
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

# csvファイルを読み込む
filename = './tweets/tweets.csv'
csvFile = open(filename)

# 各行について処理
for row in csv.reader(csvFile):
	# データ取得（ツイートは改行除去）
	date = row[3].split(' ')[0]
	tweet = ''.join(row[5].decode('utf-8').split('\n'))

	# &lt;(<), &gt;(>), &amp;(&), &quot;(")をエスケープ
	tweet_escaped = tweet.replace('&lt;', '<')
	tweet_escaped = tweet_escaped.replace('&gt;', '>')
	tweet_escaped = tweet_escaped.replace('&amp;', '&')
	tweet_escaped = tweet_escaped.replace('&quot;', '"')

	# 特殊文字をエスケープ
	tweet_escaped = re.sub(u'[%s]' % re.escape(u'\"'),
			lambda mo: u'\\\\\\' + mo.group(),
			tweet_escaped)
	tweet_escaped = re.sub(u'[%s]' % re.escape(u'`\'$'),
			lambda mo: u'\\' + mo.group(),
			tweet_escaped)
	print "mysql -utwitter -ptwitter -Dtwitter " + \
			"-e \"insert into tweetlog (time, tweet) values (\\\"" + \
			date + "\\\",\\\"" + tweet_escaped + "\\\")\""

# csvファイルを閉じる
csvFile.close()
