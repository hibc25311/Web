# 韭菜可以獲取虛擬幣及挖礦相關資訊的網站


Coin Price頁面以celery定時從幣安api獲取虛擬幣價格數據，並儲存進資料庫，同時將該筆數據以websocket的連接更新到頁面

Gpumining 頁面列出GPU的收益及成本，可在此頁面簡易計算出利潤

Crypto News頁面使用celery定時以BeautifulSoup解析幣安的新聞頁面<https://www.binance.com/en/news/top>，擷取出新聞資料並儲存進資料庫，並以發佈時間依序條列


## 如何使用：
以EC2 ubuntu 22.04為例

0. 需要docker、docker-compose、nginx，若未安裝可參考以下步驟，在終端機中輸入

    * 安裝docker
    
		`sudo apt install docker.io`
	
    * 安裝docker-compose
     
	 	`sudo apt-get install docker-compose`
	
    * 安裝nginx 
    	
		`sudo apt install nginx`
	
	1. 在 /etc/nginx/sites-available/default 內編輯
		```
        location / {
			proxy_pass http://0.0.0.0:8000/;
			proxy_set_header Host $host;
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_set_header X-Forwarded-Proto $scheme;
			proxy_set_header Upgrade $http_upgrade;
			proxy_set_header Connection "upgrade";        
			}
		```			
	2. 重啟nginx
		
		`sudo systemctl restart nginx`
		
1. 從本專案頁面將檔案下載

	`git clone https://github.com/hibc25311/Web.git`

2. 切換至專案資料夾

	`cd Web	(or working folder)`

3. 在背景啟用docker-compose

	`docker-compose up –d`

4. 進入web容器(web_chive_web_1)

	`sudo docker exec -it web_chive_web_1 bash`
	1. 進行database migrations
		
		`python manage.py makemigrations`
		
		`python manage.py migrate`
	2. 建立一個django superuser依照指示輸入使用者及密碼
	
		`python manage.py createsuperuser`
	
	3. 獲取價格數據、幣安新聞以celery定時運作

		`celery -A chive_web worker -l info -B`
5. 至此可連接http://”EC2公有IPv4地址” 瀏覽，例如 <http://54.218.124.31/>，其中Coin Price及Crypto News應有資料，Gpumining尚無資訊
6. 連結http://”EC2公有IPv4地址”/admin，並參考下列網址手動建立GPU以在Gpumining頁面示範
	
	參考GPU及算力資訊<https://whattomine.com/>
	



		
