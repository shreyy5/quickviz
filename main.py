def abc(user_input):
    import os

    from groq import Groq

    client = Groq(
        api_key="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"
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """You are a SQL assistent which takes user query in natural language and generate the sql query. the table name is sales and it has 18 colums
                [product_id, product_name, category, price, review_score, review_count, sales_month_1 to sales_month_12] Generate the production ready sql query in double quotes with no explanation""",
            },
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama3-70b-8192",
    )

    q = (chat_completion.choices[0].message.content)

    import mysql.connector 
    import logging
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="quickviz"
    )

    mycursor = mydb.cursor()
    query=""
    for i in range(len(q)):
        if(q[i].lower()=='s'):
            while(q[i]!=';'):
                query+=q[i]
                i+=1
            break
    
    # return query 
# + str("SHOW TABLES"==query)

    mycursor.execute(query)

    myresult = mycursor.fetchall()
    return myresult
    # for x in myresult:
    #     print(x)