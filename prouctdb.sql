-- データベースの選択または作成
CREATE DATABASE IF NOT EXISTS productdb;
USE productdb;

-- 商品テーブルの作成
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    product_code BIGINT PRIMARY KEY,
    product_name VARCHAR(50),
    price INT
);

-- テーブル全体の文字セットを変更
ALTER TABLE products CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- データの挿入
INSERT INTO products (product_code, product_name, price) VALUES (107523028, 'あきたこまち', 3000);
INSERT INTO products (product_code, product_name, price) VALUES (107413119, 'あきほなみ', 3000);
INSERT INTO products (product_code, product_name, price) VALUES (108452145, 'いちほまれ', 3000);
INSERT INTO products (product_code, product_name, price) VALUES (108378959, 'おいでまい', 2400);
INSERT INTO products (product_code, product_name, price) VALUES (108374862, 'きぬむすめ', 2700);
INSERT INTO products (product_code, product_name, price) VALUES (108319394, 'コシヒカリ', 2600);
INSERT INTO products (product_code, product_name, price) VALUES (108390342, '青天の霹靂', 3200);
INSERT INTO products (product_code, product_name, price) VALUES (107929298, 'つや姫', 3000);
INSERT INTO products (product_code, product_name, price) VALUES (107185556, 'ななつぼし', 2600);
INSERT INTO products (product_code, product_name, price) VALUES (108128725, 'ひとめぼれ', 2900);
INSERT INTO products (product_code, product_name, price) VALUES (108576746, '森のくまさん', 3000);
INSERT INTO products (product_code, product_name, price) VALUES (107800826, 'ゆめぴりか', 3000);
INSERT INTO products (product_code, product_name, price) VALUES (108872315, '富富富', 3500);
INSERT INTO products (product_code, product_name, price) VALUES (108661633, 'ヒノヒカリ', 2500);
INSERT INTO products (product_code, product_name, price) VALUES (108987891, '銀河のしずく', 2600);

-- データの確認
SELECT * FROM products;