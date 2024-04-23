import mysql.connector
import streamlit as st
import pandas as pd
# Establish a connection to MySQL Server

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="d33p@2324",
    database="movie_db"
)

mycursor = mydb.cursor()
print("Connection Established")

# Create Streamlit App


def main():
    st.title("MOVIEEESS")

    # Display Options for CRUD Operations
    option = st.sidebar.selectbox(
        "Select an Operation", ("Add", "Show", "Update", "Delete"))
    # Perform Selected CRUD Operations
    if option == "Add":
        st.subheader("Add a movie")
        name = st.text_input("Title")
        year = st.text_input("Release Year")
        director = st.text_input("Director")
        genre = st.text_input("Genre")
        if st.button("Create"):
            sql = "insert into movies(title,year,director,genre) values(%s,%s,%s,%s)"
            val = (name, year, director, genre)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!!!")

    elif option == "Show":
        st.subheader("List of Movies")

        # Execute the SQL query to fetch movies from the database
        mycursor.execute("SELECT * FROM movies")
        result = mycursor.fetchall()

        # Check if there are any movies in the result
        if result:
            # Convert result to a list of dictionaries for easier display
            movies_list = [{'ID': row[0], 'Title': row[1], 'Year': str(
                row[2]), 'Director': row[3], 'Genre': row[4]} for row in result]

            # Convert the list of dictionaries to a pandas DataFrame
            df = pd.DataFrame(movies_list)

            # Reset the index of the DataFrame to remove the default index column
            df.reset_index(drop=True, inplace=True)

            # Display movies in table format
            st.write(df)
        else:
            st.write("No movies found in the database.")

    elif option == "Update":
        st.subheader("Update a Record")
        id = st.number_input("Enter ID", min_value=1)
        name = st.text_input("Title")
        year = st.text_input("Release Year")
        director = st.text_input("Director")
        genre = st.text_input("Genre")
        if st.button("Update"):
            sql = "update movies set title=%s, year=%s, director=%s, genre=%s where id =%s"
            val = (name, year, director, genre, id)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")

    elif option == "Delete":
        st.subheader("Delete a Record")
        id = st.number_input("Enter ID", min_value=1)
        if st.button("Delete"):
            sql = "delete from movies where id =%s"
            val = (id,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")


if __name__ == "__main__":
    main()
