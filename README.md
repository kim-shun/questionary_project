# README
 
# アプリケーション名
## Unique Questionary

# 目指した課題解決
解決したい課題は、アンケートの結果における「参考にしにくい評価内容」である。

インターネットが普及した現代では、飲食店や美容院といったサービスを利用する前に、そのサービスの「評価」を調べる人が多い。

その評価を形成するのがアンケートであるが、わざわざアンケートに回答するという行為に対して、消費者が十分なモチベーションを抱くことは期待できない。また回答者にも偏りがあり、高い精度で言語化された評価を見かけることはなかなかないと言える。事実私は、一定以上評価されているサービスを区別して、どのサービスが自分に相応しいかを見極めることがなかなかできない。

そこで私は「自発的もしくは自然にアンケートに回答したくなる仕組み」、「サービスごとに区別しやすい評価基準、評価指標の設定」、「データのばらつきの可視化」、「回答者の言語化の負担を軽減させる質問設計」などが必要だと考える。

「自発的もしくは自然にアンケートに回答したくなる仕組み」の具体例には、レシートのゴミ箱がアンケート投票箱になっているといったことが挙げられる。また「サービスごとに区別しやすい評価基準、評価指標の設定」とは、飲食店の総合評価だけでなく「接客レベル」、「料理の味」、「座席の防音性」といった指標からサービスを区別できるようにするといったことだ。「データのばらつきの可視化」のためには中央値と母数を明記し、「回答者の言語化の負担を軽減させる」ためには、ユーザーの傾向を網羅できる厳選された選択肢で回答させることができるだろう。

今回は第一段階として、評価全般を星5つではなく1~100点で判定させる一方で中央値と母数も可視化することと、選択肢を厳選させることにこだわった、質問作成と回答ができるアプリを作ってみることにした。

ゆくゆくは質問作成を円滑に進めるためのワード予測変換のアルゴリズムを組み込みたい。




# 基本機能
- ユーザー管理機能
- 質問ジャンル登録機能
- 質問作成機能
- 質問一覧表示機能
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
- 質問作成時の言語化フォロー機能
- ラジオボタンの初期値設定
- 性別・年齢等の一般的な質問の追加可否を問う項目
- 複数選択項目を設けるか考える
- 選択肢の数を可変できるようにするか考える




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
