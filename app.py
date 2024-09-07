from flask import Flask, render_template, redirect, url_for, session, flash , request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Email

from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'annipol2001'
app.config['MYSQL_DB'] = 'ferrydb'
app.secret_key = 'many random bytes'

mysql = MySQL(app)



# class ticket(FlaskForm):
#     source = StringField("source",validators=[DataRequired()])
#     dest = StringField("dest",validators=[DataRequired()])
#     travelDate = StringField("travelDate",validators=[DataRequired()])
#     availabeSeats = StringField("availabeSeats",validators=[DataRequired()])
#     bookingStatus = StringField("bookingStatus",validators=[DataRequired()])
    
#     submit = SubmitField("ticket")

    
# class details(FlaskForm):
#     passID = StringField(" passID",validators=[DataRequired()])
#     AssociatedTicketID = StringField("AssociatedTicketID",validators=[DataRequired()])
#     name = StringField("name",validators=[DataRequired()])
#     age = StringField("age",validators=[DataRequired()])
#     phone = StringField("phone",validators=[DataRequired()])
#     email = StringField("Email",validators=[DataRequired(), Email()])    
#     address = StringField("address",validators=[DataRequired()])
#     nationality = StringField("nationality",validators=[DataRequired()])   
#     bloodgroup = StringField("bloodgroup",validators=[DataRequired()])
#     gender = StringField("gender",validators=[DataRequired()])  
#     food = StringField("food",validators=[DataRequired()])  
#     submit = SubmitField("detail")


# class booking(FlaskForm):
#     source = StringField("source",validators=[DataRequired()])
#     dest = StringField("dest",validators=[DataRequired()])
#     travelDate = StringField("travelDate",validators=[DataRequired()])
#     totalpass = StringField("totalpass",validators=[DataRequired()])
#     bookingStatus = StringField("bookingStatus",validators=[DataRequired()])
#     bookingClass = StringField("bookingClass",validators=[DataRequired()])
#     passmobnum = StringField("passmobnum",validators=[DataRequired()])
#     submit = SubmitField("booking")



@app.route('/',methods=['POST','GET'])
def Ticket():
    #  form = ticket()
    #  if form.validate_on_submit():
     if request.method == 'POST': 
            # source = form.source.data
            # dest= form.dest.data
            # travelDate = form.travelDate.data
            # availabeSeats = form.availabeSeats.data
            # bookingStatus = form.bookingStatus.data
            source =request.form['source']
            dest =request.form['dest']
            travelDate =request.form['travelDate']
            availabeSeats =request.form['availabeSeats']
            bookingStatus =request.form['bookingStatus']

            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO bookingavailability (source,dest,travelDate,availabeSeats,bookingStatus) VALUES (%s,%s,%s,%s,%s)",
                            (source,dest,travelDate,availabeSeats,bookingStatus))
            mysql.connection.commit()
            cursor.close()

            return redirect('/detail')
     return render_template('ticket.html')



@app.route('/detail', methods=['POST','GET'])
def detail():
    #  form = details()
    #  if form.validate_on_submit():
        
    #     PassengerName = form.PassengerName.data
    #     Age = form.Age.data
    #     phone = form.phone.data
    #     Address = form.Address.data
    #     Nationality =form.Nationality.data
    #     BloodGroup = form.BloodGroup.data
    #     Gender = form.Gender.data
    #     FoodPreferences = form.FoodPreferences.data
        # store data into database 
    if request.method == 'POST':    

        PassengerName =request.form['PassengerName']
        Age =request.form['Age']
        phone =request.form['phone']
        Address =request.form['Address']
        Nationality =request.form['Nationality']
        BloodGroup =request.form['BloodGroup']
        Gender =request.form['Gender']
        FoodPreferences =request.form['FoodPreferences']
         
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO passengerdetails (PassengerName,Age,phone,Address,Nationality,BloodGroup,Gender,FoodPreferences) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                        (PassengerName,Age,phone,Address,Nationality,BloodGroup,Gender,FoodPreferences))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('book.html'))
    return render_template('detail.html')



@app.route('/book',methods=['POST','GET'])
def book():
    #  form = booking()
    #  if form.validate_on_submit():
    #         source = form.source.data
    #         dest= form.dest.data
    #         travelDate = form.travelDate.data
    #         totalpass = form.totalpass.data
    #         bookingStatus = form.bookingStatus.data
    #         bookingClass = form.bookingClass.data
    #         passmobnum= form.passmobnum.data
    if request.method == 'GET':        
            source =request.form['source']
            dest =request.form['dest']
            travelDate =request.form['travelDate']
            totalpass =request.form['totalpass']
            bookingStatus =request.form['bookingStatus']
            bookingClass =request.form['bookingClass']
            passmobnum =request.form['passmobnum']

            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO ticketbooking (source,dest,travelDate,totalpass,bookingStatus,bookingClass,passmobnum) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                            (source,dest,travelDate,totalpass,bookingStatus,bookingClass,passmobnum))
            mysql.connection.commit()
            cursor.close()

            return redirect(url_for('detail.html'))
    return render_template('book.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)
