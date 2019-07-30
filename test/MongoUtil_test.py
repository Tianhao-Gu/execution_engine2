# -*- coding: utf-8 -*-
import unittest
import os
from configparser import ConfigParser

from test.mongo_test_helper import MongoTestHelper
from execution_engine2.utils.MongoUtil import MongoUtil


class MongoUtilTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        config_file = os.environ.get(
            "KB_DEPLOYMENT_CONFIG", os.path.join("test", "deploy.cfg")
        )
        config_parser = ConfigParser()
        config_parser.read(config_file)

        cls.config = {}
        for nameval in config_parser.items("execution_engine2"):
            cls.config[nameval[0]] = nameval[1]

        cls.config["mongo-collection"] = "jobs"

        cls.mongo_helper = MongoTestHelper()
        cls.test_collection = cls.mongo_helper.create_test_db(
            db=cls.config["mongo-database"], col=cls.config["mongo-collection"]
        )
        cls.mongo_util = MongoUtil(cls.config)

    @classmethod
    def tearDownClass(cls):
        print("Finished testing MongoUtil")

    def getMongoUtil(self):
        return self.__class__.mongo_util

    # def test_get_collection(self):
    #     mongo_util = self.getMongoUtil()
    #     with self.assertRaises(ValueError) as context:
    #         mongo_util._get_collection(
    #             "fake_mongo_host", 1234, "mongo_database", "mongo_collection"
    #         )

    #     self.assertIn("Connot connect to Mongo server", str(context.exception.args))

    def test_init_ok(self):
        class_attri = [
            "mongo_host",
            "mongo_port",
            "mongo_database",
            "mongo_collection",
            "mongo_user",
            "mongo_pass",
            "mongo_authmechanism",
            "job_col",
        ]
        mongo_util = self.getMongoUtil()
        self.assertTrue(set(class_attri) <= set(mongo_util.__dict__.keys()))

        job_col = mongo_util.job_col
        self.assertEqual(job_col.name, "jobs")
        self.assertEqual(job_col.count_documents({}), 0)

    # def test_find_in_ok(self):
    #     self.start_test()
    #     mongo_util = self.getMongoUtil()

    #     # test query 'hid' field
    #     elements = ['KBH_68020', 'KBH_68022', 'fake_id']
    #     docs = mongo_util.find_in(elements, 'hid')
    #     self.assertEqual(docs.count(), 2)

    #     # test query 'hid' field with empty data
    #     elements = [0]
    #     docs = mongo_util.find_in(elements, 'hid')
    #     self.assertEqual(docs.count(), 0)

    #     # test query 'id' field
    #     elements = ['b753774f-0bbd-4b96-9202-89b0c70bf31c']
    #     docs = mongo_util.find_in(elements, 'id')
    #     self.assertEqual(docs.count(), 1)
    #     doc = docs.next()
    #     self.assertFalse('_id' in doc.keys())
    #     self.assertEqual(doc.get('hid'), 'KBH_68020')

    #     # test null projection
    #     elements = ['b753774f-0bbd-4b96-9202-89b0c70bf31c']
    #     docs = mongo_util.find_in(elements, 'id', projection=None)
    #     self.assertEqual(docs.count(), 1)
    #     doc = docs.next()
    #     self.assertEqual(doc.get('_id'), 'KBH_68020')
    #     self.assertEqual(doc.get('hid'), 'KBH_68020')

    # def test_update_one_ok(self):
    #     self.start_test()
    #     mongo_util = self.getMongoUtil()

    #     elements = ['b753774f-0bbd-4b96-9202-89b0c70bf31c']
    #     docs = mongo_util.find_in(elements, 'id', projection=None)
    #     self.assertEqual(docs.count(), 1)
    #     doc = docs.next()
    #     self.assertEqual(doc.get('created_by'), 'tgu2')

    #     update_doc = copy.deepcopy(doc)
    #     new_user = 'test_user'
    #     update_doc['created_by'] = new_user

    #     mongo_util.update_one(update_doc)

    #     docs = mongo_util.find_in(elements, 'id', projection=None)
    #     new_doc = docs.next()
    #     self.assertEqual(new_doc.get('created_by'), new_user)

    #     mongo_util.update_one(doc)

    # def test_insert_one_ok(self):
    #     self.start_test()
    #     mongo_util = self.getMongoUtil()
    #     self.assertEqual(mongo_util.handle_collection.find().count(), 10)

    #     doc = {'_id': 9999, 'hid': 9999, 'file_name': 'fake_file'}
    #     counter = mongo_util.get_hid_counter()
    #     mongo_util.insert_one(doc)
    #     new_counter = mongo_util.get_hid_counter()
    #     self.assertEqual(new_counter, counter + 1)

    #     self.assertEqual(mongo_util.handle_collection.find().count(), 11)
    #     elements = [9999]
    #     docs = mongo_util.find_in(elements, 'hid', projection=None)
    #     self.assertEqual(docs.count(), 1)
    #     doc = docs.next()
    #     self.assertEqual(doc.get('hid'), 9999)
    #     self.assertEqual(doc.get('file_name'), 'fake_file')

    #     mongo_util.delete_one(doc)
    #     self.assertEqual(mongo_util.handle_collection.find().count(), 10)

    # def test_delete_one_ok(self):
    #     self.start_test()
    #     mongo_util = self.getMongoUtil()
    #     docs = mongo_util.handle_collection.find()
    #     self.assertEqual(docs.count(), 10)

    #     doc = docs.next()
    #     hid = doc.get('hid')
    #     mongo_util.delete_one(doc)
    #     self.assertEqual(mongo_util.handle_collection.find().count(), 9)

    #     docs = mongo_util.find_in([hid], 'hid', projection=None)
    #     self.assertEqual(docs.count(), 0)

    #     mongo_util.insert_one(doc)
    #     self.assertEqual(mongo_util.handle_collection.find().count(), 10)
    #     docs = mongo_util.find_in([hid], 'hid', projection=None)
    #     self.assertEqual(docs.count(), 1)

    # def test_delete_many_ok(self):
    #     self.start_test()
    #     mongo_util = self.getMongoUtil()
    #     docs = mongo_util.handle_collection.find()
    #     self.assertEqual(docs.count(), 10)

    #     docs_to_delete = list()
    #     docs_to_delete.append(docs.next())
    #     docs_to_delete.append(docs.next())
    #     docs_to_delete = docs_to_delete * 2  # test delete duplicate items
    #     deleted_count = mongo_util.delete_many(docs_to_delete)
    #     self.assertEqual(deleted_count, 2)
    #     self.assertEqual(mongo_util.handle_collection.find().count(), 8)
    #     docs = mongo_util.find_in([doc.get('hid') for doc in docs_to_delete], 'hid')
    #     self.assertEqual(docs.count(), 0)

    #     for doc in docs_to_delete:
    #         try:
    #             mongo_util.insert_one(doc)
    #         except Exception:
    #             pass
    #     self.assertEqual(mongo_util.handle_collection.find().count(), 10)
    #     docs = mongo_util.find_in([doc.get('hid') for doc in docs_to_delete], 'hid')
    #     self.assertEqual(docs.count(), 2)
