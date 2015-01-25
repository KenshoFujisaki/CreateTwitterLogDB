# CreateTwitterLogDB

個人のツイート情報をDB（MySQL）に格納します．

## 手順

1. Tweetデータのダウンロード  
    1. Twitter → 設定 → [ユーザー情報](https://twitter.com/settings/account)を開く  
    2. 全ツイート履歴 から ダウンロード  
    3. ダウンロードしたzipファイルを展開し，その中に含まれる「tweets.csv」を「./tweets/tweets.csv」に配置する

2. MySQLのユーザー登録・データベースへの権限付与・データベースの作成  
    ```sh
    $ mysql -u root -p
    ```
    ```sql
    > CREATE USER 'twitter'@'localhost' IDENTIFIED BY 'twitter';
    > GRANT ALL PRIVILEGES ON twitter.* TO 'twitter'@'localhost' IDENTIFIED BY 'twitter';
    > CREATE DATABASE twitter CHARACTER SET utf8;
    > USE twitter;
    > CREATE TABLE tweetlog ( id INT(11) NOT NULL AUTO_INCREMENT, time DATE, tweet VARCHAR(256), PRIMARY KEY (id) );
    > exit;
    ```

3. TweetデータのMySQL格納
    ```sh
    $ python ./tweets.csv2mysql.py | sh +x
    ```
