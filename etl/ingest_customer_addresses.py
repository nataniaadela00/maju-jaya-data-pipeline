import pandas as pd
from sqlalchemy import create_engine
import time
	
# koneksi mysql
db_url = "mysql+pymysql://root:admin123@mysql:3306/maju_jaya"
engine = None

# retry connection
for i in range(10):
    try:
        engine = create_engine(db_url)
        conn = engine.connect()
        conn.close()
        print("Connected to MySQL")
        break
    except Exception as e:
        print("MySQL belum ready, retry 5 detik...")
        time.sleep(5)
	
# baca csv
df = pd.read_csv(
    "data/customer_addresses.csv",
    sep=",",
    header=0
)
df.columns = [
	"id",
	"customer_id",
	"address",
	"city",
	"province",
	"created_at"
	]
	
df = df.iloc[1:]
	
# insert ke mysql
df.to_sql(
 	"customer_addresses",
	con=engine,
	if_exists="append",
	index=False
	)
	
print("Data berhasil di-ingest ke MySQL")
