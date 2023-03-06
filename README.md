# README
 
# アプリケーション名
## Unique Questionary

# 基本機能
- ユーザー管理機能
- 質問ジャンル登録機能
- 質問作成機能
- 質問一覧表示機能
- 回答機能

# 実装予定の機能
- ラベル名、説明文をユーザー目線に修正
- 質問作成機能内でのジャンル登録機能
- バリデーション
- 回答詳細表示機能
- 集計結果へのコメント機能
- 質問検索機能
- 排他制御
- トランザクション制御
- 質問削除機能
- 削除取り消し機能
- 一括登録機能
- 変更履歴ダウンロード
- ユーザーのニックネーム他詳細情報登録機能
- テーブル定義見直し(genre→question、回答内容の登録方法、不要な外部キー削除など)
- 冗長なコードのリファクタリング
- テキストボックスサイズの調整
- css(背景色)の調整
- 総合点の概念の見直し
- placeholder
- ログとコメントの埋め込み
- 質問作成時の言語化フォロー機能




# テーブル設計

## ER図
添付予定

## customUser テーブル

## m_genre テーブル
| Column                 | Type       | Options                        |
| ------                 | ------     | -----------                    |
| genre_name             | string     | null: false, unique: true      |
| delete_flag            | integer    | null: false                    |
| created_at             | date       |                                |
| updated_at             | date       |                                |
| user                   | references | foreign_key: true              |


### Association
- belongs_to :user
- has_many   :question

## question テーブル

| Column                 | Type       | Options                        |
| ------                 | ------     | -----------                    |
| title                  | string     | null: false, unique: true      |
| genre                  | references | foreign_key: true, null: false |
| answer_num             | integer    | null: false                    |
| answer_count           | integer    | null: false                    |
| median_score           | integer    | null: false                    |
| average_score          | integer    | null: false                    |
| delete_flag            | integer    | null: false                    |
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
| question               | references | foreign_key: true, null: false |
| question_order         | integer    | null: false                    |
| answer_type            | string     | null: false                    |
| content                | text       | null: false                    |
| delete_flag            | integer    | null: false                    |
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
| question               | references | foreign_key: true, null: false |
| question_detail        | references | foreign_key: true, null: false |
| choice_item            | string     | null: false                    |
| delete_flag            | integer    | null: false                    |
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
| question               | references | foreign_key: true, null: false |
| all_score              | integer    | null: false                    |
| comment                | text       | null: true                     |
| delete_flag            | integer    | null: false                    |
| created_at             | date       |                                |
| updated_at             | date       |                                |
| user                   | references | foreign_key: true              |


### Association
- belongs_to :user
- belongs_to :question
- has_many   :answer_detail

## answer_detail テーブル
| Column                 | Type       | Options                        |
| ------                 | ------     | -----------                    |
| question               | references | foreign_key: true, null: false |
| question_detail        | references | foreign_key: true, null: false |
| answer                 | references | foreign_key: true, null: false |
| content                | string     | null: false                    |
| delete_flag            | integer    | null: false                    |
| created_at             | date       |                                |
| updated_at             | date       |                                |
| user                   | references | foreign_key: true              |


### Association
- belongs_to :user
- belongs_to :question
- belongs_to :question_detail
- belongs_to :answer
