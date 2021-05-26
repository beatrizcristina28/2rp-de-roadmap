from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.dataframe import DataFrame
import pyspark.sql.functions

sc = SparkContext()
spark = SparkSession(sc)

#carregar os dados da tabela pokemon_beatriz em um dataframe
pokemons = spark.table("work_dataeng.pokemon_beatriz")

#carregar os dados da tabela generation_beatriz em um dataframe
generation = spark.table("work_dataeng.generation_beatriz")

#filtrar o dataframe com os catdados de generation que obedecam a condicao
generation_filtered = generation.filter(generation['date_introduced'] < '2002-11-21')

#realizar um cache do dataframe
generation_filtered = generation_filtered.cache()

#join entre os dataframes
#necessario alterar o nome da coluna para nao duplicar
pokemons = pokemons.withColumnRenamed('generation', 'generation_pokemons')
pokemon_generation_join = pokemons.join(generation_filtered, on=[pokemons.generation_pokemons == generation_filtered.generation], how='inner')

#criar uma tabela temporaria antes de criar a tabela no hive
pokemon_generation_join.createOrReplaceTempView("pokemon_generation_join_temp")
spark.sql("CREATE TABLE IF NOT EXISTS work_dataeng.pokemons_oldschool_beatriz as select * from pokemon_generation_join_temp")