from model_generator_pyramid import BaseModelGenerator, Params

params = Params()
params.dialect = 'mysql'
params.user = 'roboshopuser'
params.password = 'howcute121'
params.host = '192.168.1.55'
params.db_name = 'roboshop'

params.user = 'root'
params.password = 'howcute121'
params.host = '192.168.2.53'
params.db_name = 'mm'

# params.user = 'root'
# params.password = 'mysql56forkitch'
# params.host = '127.0.0.1'
# params.db_name = 'hangbiaodeng'


#schema for db / could be None for default
params.schema = None

#if true Raise exception if a PK is not present in the table
params.force_pk = False

#specify the tables you want to generate the model for.
params.table_list = params.fetch_all_tables_pg(params)
params.table_list = ["client_store", "client_store_activity", 
                     "client_store_act_stores", "client_store_act_products"]
#params.metadata_name = 'ev5_metadata'

bmg = BaseModelGenerator(params)

bmg.generate_model()
