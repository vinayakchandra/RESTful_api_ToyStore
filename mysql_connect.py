import mysql.connector as mc


class ConnectSql:
    mydb = mc.connect(host="localhost", user="root", password="", database="REST_API")
    myCursor = mydb.cursor()
    myResult = ""

    # Sql functions
    # insert
    def insertToy(self, id: int, name, price: int):
        self.myCursor.execute(f"INSERT INTO TOY_STORE(toy_id, toy_name, toy_price) VALUES( {id}, '{name}', {price} );")
        # self.myCursor.execute(f"-- INSERT INTO TOY_STORE(toy_id, toy_name, toy_price) VALUES(3, 'rabbit', 400);")
        self.mydb.commit()
        return self.myCursor

    # show all entries
    def showToyAll(self):
        self.myCursor.execute(f"select * from toy_store;")
        self.myResult = self.myCursor.fetchall()
        return self.myResult

    # show entry of an id
    def showToy(self, id):
        self.myCursor.execute(f"select * from toy_store WHERE toy_id = {id};")
        self.myResult = self.myCursor.fetchall()
        return self.myResult

    # delete a entry
    def deleteToy(self, id):
        self.myCursor.execute(f"DELETE FROM toy_store WHERE toy_id = {id};")
        self.mydb.commit()
        return self.myCursor

    # update a entry
    def updateToy(self, id: int, price: int):
        self.myCursor.execute(f"UPDATE toy_store SET toy_price = {price} WHERE toy_id = {id};")
        # if img is not None:
        #     updateImg(id, img)
        self.mydb.commit()
        return self.myCursor

    # update img
    def updateImg(self, id, link):
        self.myCursor.execute(f"UPDATE toy_store SET img_link = '{link}' WHERE toy_id = {id};")
        self.mydb.commit()
        return self.myCursor
