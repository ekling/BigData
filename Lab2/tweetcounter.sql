CREATE TABLE raw_tweet (tweet STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\n'
LOCATION '/input/';

CREATE TABLE tweets_text (text STRING);

INSERT OVERWRITE TABLE tweets_text
SELECT get_json_object(raw_tweet.tweet, '$.text') from raw_tweet
WHERE tweet != "" AND get_json_object(raw_tweet.tweet, '$.retweeted_status') IS NULL;

SELECT w, count(*)
FROM tweets_text LATERAL VIEW explode(split(lower(text), " ")) lTable as w
WHERE w = "han" OR w = "hon" OR w = "den" OR w = "det" OR w = "denna" OR w = "denne" OR w = "hen"
GROUP BY w;
