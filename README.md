# README
 
# アプリケーション名
## Unique Questionary

# アプリの作成目的

このアプリを作成する目的は、アンケート回答者の所感を、忠実に言語化させることにあります。
自由なコメントには委ねず、「選択肢の厳選」と「高精度の予測変換(サジェスト機能)」でその実現を目指します。

飲食店や美容院といったサービスの多くは、「5段階の星の数」と「コメント」で評価されることがほとんどです。
それには「回答しやすい」といったメリットがあります。また安易に評価の総数に対する平均を取らず、独自のアルゴリズムを構築することで
評価内容の信用性を確保していることだと思います。

一方で「5段階評価」だと、同じ人物が複数のサービスを評価する場合、それぞれのサービスの序列を明確にしにくいといったデメリットがあります。また「コメント」では、アンケート回答者の言葉の引き出しの中でしか、所感を表現できません。

そこで、あらかじめ予測できる所感を「厳選された選択肢」と「予測変換」で提示してあげたり、飲食店の総合評価だけでなく「接客レベル」、「料理の味」、「座席の防音性」といった指標からでもサービスを区別できるようにしたりすることを考えました。また星5つではなく1~100点で判定させる一方で、中央値と母数も可視化し、全集計データをグラフで表示してあげたりすることで、より消費者にとって参考になるアンケート結果になるのではないかということも考えています。「5段階評価」が採用される理由の1つにはおそらくデータのばらつきを防ぐ目的があるかと思いますが、全集計データのグラフ化の方法を工夫し、ばらつきのあるデータを消費者にわかる形にしたい狙いがあります。

もちろん、そもそもアンケートに回答する行為に高いモチベーションを抱けないといった課題もありますが、それは別課題として考え、まずはアンケート回答者の所感を忠実に言語化させ、閲覧者に参考になる評価結果を出力できるアプリの作成を実現させます。



# 基本機能
- ユーザー管理機能
- 質問ジャンル登録機能
- 質問作成機能
- 質問一覧表示機能
- 回答機能
- 回答集計結果表示機能

# 利用方法
- ユーザー登録  
- 質問一覧表示機能
- 質問作成機能
ヘッダーの「CREATE QUESTION」を押下。アンケートのタイトルを入力し、アンケートのジャンルを選択する。質問内容を1から5まで考えて入力し、それぞれの質問に対する回答方法を次の3つから選択する。「点数(0~100点)で評価させる」、「あてはまるか、あてはまらないかを選択させる」、「作成した選択肢から選ばせる」。質問内容1は必須入力で、「作成した選択肢から選ばせる」を選択した場合、選択肢1と選択肢2も必須入力。
- 回答機能
- 回答集計結果表示機能

# 実装した機能
## 質問一覧表示機能(初期表示画面)
[![Image from Gyazo](https://i.gyazo.com/bcd762f9326349a3da5e63dffcd6a88f.gif)](https://gyazo.com/bcd762f9326349a3da5e63dffcd6a88f)

## 質問作成機能
[![Image from Gyazo](https://i.gyazo.com/61e9561c1b8f37736c178651ae3ef7e0.gif)](https://gyazo.com/61e9561c1b8f37736c178651ae3ef7e0)

## 回答機能
[![Image from Gyazo](https://i.gyazo.com/f50b34ff92e4469bdb6449eb1c1c6dd1.gif)](https://gyazo.com/f50b34ff92e4469bdb6449eb1c1c6dd1)

## 回答集計結果表示機能
- 実装中

# 実装予定の機能
- ラベル名、説明文をユーザー目線に修正
- 質問作成機能内でのジャンル登録機能
- バリデーション
- 質問作成時の言語化フォロー機能(予測変換、サジェスト機能)
- 回答集計結果表示機能
- 集計結果へのコメント機能
- 質問検索機能
- 排他制御
- トランザクション制御
- 質問削除機能
- 削除取り消し機能
- 一括登録機能
- 変更履歴ダウンロード
- ユーザーのニックネーム他詳細情報登録機能
- 冗長なコードのリファクタリング
- ログとコメントの埋め込み
- ラジオボタンの初期値設定
- 性別・年齢等の一般的な質問の追加可否を問う項目
- 質問項目・選択肢の数を設定する機能




# テーブル設計

## ER図
[![Image from Gyazo](https://i.gyazo.com/f144f12d53638398f64b4d74ca216dea.png)](https://gyazo.com/f144f12d53638398f64b4d74ca216dea)

## customuser テーブル
| Column                 | Type       | Options                        |
| ------                 | ------     | -----------                    |
| id                     | integer    | null: false, primary_key: true |
| password               | string     | null: false                    |
| last_login             | date       |                                |
| is_superuser           | boolean    | null: false                    |
| username               | string     | null: false                    |
| first_name             | string     | null: false                    |
| last_name              | string     | null: false                    |
| email                  | string     | null: false                    |
| is_staff               | boolean    | null: false                    |
| is_active              | boolean    | null: false                    |
| date_joined            | date       | null: false                    |


### Association
- has_many   :m_genre
- has_many   :question
- has_many   :question_detail
- has_many   :m_choice
- has_many   :answer
- has_many   :answer_detail

## m_genre テーブル
| Column                 | Type       | Options                        |
| ------                 | ------     | -----------                    |
| id                     | integer    | null: false, primary_key: true |
| genre_name             | string     | null: false, unique: true      |
| delete_flag            | string     | null: false                    |
| created_at             | date       |                                |
| updated_at             | date       |                                |
| user                   | references | foreign_key: true              |


### Association
- belongs_to :user
- has_many   :question

## question テーブル

| Column                 | Type       | Options                        |
| ------                 | ------     | -----------                    |
| id                     | integer    | null: false, primary_key: true |
| title                  | string     | null: false, unique: true      |
| genre                  | references | foreign_key: true, null: false |
| score_flag             | string     | null: false                    |
| answer_num             | integer    | null: false                    |
| answer_count           | integer    | null: false                    |
| median_score           | float      | null: false                    |
| average_score          | float      | null: false                    |
| delete_flag            | string     | null: false                    |
| created_at             | date       |                                |
| updated_at             | date       |                                |
| user                   | references | foreign_key: true              |


### Association
- belongs_to :user
- belongs_to :m_genre
- has_many   :question_detail
- has_many   :answer
- has_many   :answer_detail
- has_many   :m_choice

## question_detail テーブル
| Column                 | Type       | Options                        |
| ------                 | ------     | -----------                    |
| id                     | integer    | null: false, primary_key: true |
| question               | references | foreign_key: true, null: false |
| question_order         | integer    | null: false                    |
| answer_type            | string     | null: false                    |
| content                | text       | null: false                    |
| delete_flag            | string     | null: false                    |
| created_at             | date       |                                |
| updated_at             | date       |                                |
| user                   | references | foreign_key: true              |


### Association
- belongs_to :user
- belongs_to :question
- has_many   :answer_detail
- has_many   :m_choice

## m_choice テーブル
| Column                 | Type       | Options                        |
| ------                 | ------     | -----------                    |
| id                     | integer    | null: false, primary_key: true |
| question               | references | foreign_key: true, null: false |
| question_detail        | references | foreign_key: true, null: false |
| choice_item            | string     | null: false                    |
| delete_flag            | string     | null: false                    |
| created_at             | date       |                                |
| updated_at             | date       |                                |
| user                   | references | foreign_key: true              |


### Association
- belongs_to :user
- belongs_to :question
- belongs_to :question_detail
- has_many   :answer_detail


## answer テーブル
| Column                 | Type       | Options                        |
| ------                 | ------     | -----------                    |
| id                     | integer    | null: false, primary_key: true |
| question               | references | foreign_key: true, null: false |
| all_score              | integer    | null: true                     |
| comment                | text       | null: true                     |
| delete_flag            | string     | null: false                    |
| created_at             | date       |                                |
| updated_at             | date       |                                |
| user                   | references | foreign_key: true              |


### Association
- belongs_to :user
- belongs_to :question
- has_many   :answer_detail

## answer_detail テーブル
| Column                  | Type       | Options                        |
| ------                  | ------     | -----------                    |
| id                      | integer    | null: false, primary_key: true |
| question                | references | foreign_key: true, null: false |
| question_detail         | references | foreign_key: true, null: false |
| answer                  | references | foreign_key: true, null: false |
| score_content           | string     | null: true                     |
| select_content          | string     | null: true                     |
| original_select_content | string     | null: true                     |
| delete_flag             | string     | null: false                    |
| created_at              | date       |                                |
| updated_at              | date       |                                |
| user                    | references | foreign_key: true              |


### Association
- belongs_to :user
- belongs_to :question
- belongs_to :question_detail
- belongs_to :answer
