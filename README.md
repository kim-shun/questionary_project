# README
 
# アプリケーション名
## Unique Questionary

# 基本機能
- ユーザー管理機能
- 質問ジャンル登録機能
- 質問作成機能
- 質問一覧表示機能
- 回答機能

# テーブル設計

## ER図
添付予定

## customUser テーブル

## question テーブル

| Column                 | Type       | Options                        |
| ------                 | ------     | -----------                    |
| title                  | string     | null: false, unique: true      |
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

## question_detail テーブル

## answer テーブル

## answer_detail テーブル

## m_genre テーブル

## m_choice テーブル

