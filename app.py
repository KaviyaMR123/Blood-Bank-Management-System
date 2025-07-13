from flask import Flask, render_template, request, redirect
import db_config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_donor', methods=['GET', 'POST'])
def add_donor():
    if request.method == 'POST':
        donor_id = request.form['donor_id']
        name = request.form['donor_name']
        phone = request.form['donor_phone']
        dob = request.form['dob']
        gender = request.form['gender']
        address = request.form['donor_address']
        weight = request.form['weight']
        bp = request.form['blood_pressure']
        iron = request.form['iron_content']
        doctor_id = request.form['doctor_id']

        conn = db_config.connect()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO Donor (Donor_id, Donor_name, Donor_Phone_no, DOB, Gender, Donor_address, Weight, Blood_pressure, Iron_content, Doctor_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (donor_id, name, phone, dob, gender, address, weight, bp, iron, doctor_id))
            conn.commit()
        except Exception as e:
            return f"Error: {e}"
        finally:
            cur.close()
            conn.close()

        return redirect('/view_donor')
    return render_template('add_donor.html')


@app.route('/view_donor')
def view_donor():
    conn = db_config.connect()  # Connect to MySQL using your config
    cur = conn.cursor()
    cur.execute("SELECT * FROM Donor")  # Fetch all donors
    donors = cur.fetchall()  # Save results to pass to template
    conn.close()  # Always close DB connection
    return render_template('view_donor.html', donors=donors)

@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        name = request.form['doctor_name']
        address = request.form['doctor_address']
        phone = request.form['doctor_phone']

        conn = db_config.connect()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO Doctor (Doctor_id, Doctor_name, Doctor_address, Doctor_Phone_no)
                VALUES (%s, %s, %s, %s)
            """, (doctor_id, name, address, phone))
            conn.commit()
        except Exception as e:
            return f"<h3>Error: {e}</h3>"
        finally:
            cur.close()
            conn.close()

        return redirect('/view_doctor')  # Go to doctor list page
    return render_template('add_doctor.html')


@app.route('/view_doctor')
def view_doctor():
    conn = db_config.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Doctor")
    doctors = cur.fetchall()
    conn.close()
    return render_template('view_doctor.html', doctors=doctors)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        name = request.form['patient_name']
        phone = request.form['patient_phone']
        address = request.form['patient_address']
        hospital = request.form['hospital_address']

        conn = db_config.connect()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO Patient (Patient_id, Patient_name, Patient_phone_no, Patient_address, Hospital_address)
                VALUES (%s, %s, %s, %s, %s)
            """, (patient_id, name, phone, address, hospital))
            conn.commit()
        except Exception as e:
            return f"<h3>Error: {e}</h3>"
        finally:
            cur.close()
            conn.close()

        return redirect('/view_patient')
    return render_template('add_patient.html')


@app.route('/view_patient')
def view_patient():
    conn = db_config.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Patient")
    patients = cur.fetchall()
    conn.close()
    return render_template('view_patient.html', patients=patients)


@app.route('/add_bloodbank', methods=['GET', 'POST'])
def add_bloodbank():
    if request.method == 'POST':
        blood_id = request.form['blood_id']
        name = request.form['name']
        address = request.form['address']

        conn = db_config.connect()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO Blood_bank (Blood_id, Blood_bank_name, Blood_Bank_address)
                VALUES (%s, %s, %s)
            """, (blood_id, name, address))
            conn.commit()
        except Exception as e:
            return f"<h3>Error: {e}</h3>"
        finally:
            cur.close()
            conn.close()

        return redirect('/view_bloodbank')
    return render_template('add_bloodbank.html')


@app.route('/view_bloodbank')
def view_bloodbank():
    conn = db_config.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Blood_bank")
    bloodbanks = cur.fetchall()
    conn.close()
    return render_template('view_bloodbank.html', bloodbanks=bloodbanks)


@app.route('/add_blood', methods=['GET', 'POST'])
def add_blood():
    if request.method == 'POST':
        blood_group = request.form['blood_group']
        donor_id = request.form['donor_id']
        blood_bank_id = request.form['blood_bank_id']

        conn = db_config.connect()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO Blood (Blood_group, Donor_id, Blood_bank_id)
                VALUES (%s, %s, %s)
            """, (blood_group, donor_id, blood_bank_id))
            conn.commit()
        except Exception as e:
            return f"<h3>Error: {e}</h3>"
        finally:
            cur.close()
            conn.close()

        return redirect('/view_blood')
    return render_template('add_blood.html')


@app.route('/view_blood')
def view_blood():
    conn = db_config.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Blood")
    bloods = cur.fetchall()
    conn.close()
    return render_template('view_blood.html', bloods=bloods)


@app.route('/add_blooddelivery', methods=['GET', 'POST'])
def add_blooddelivery():
    if request.method == 'POST':
        blood_bank_id = request.form['blood_bank_id']
        patient_id = request.form['patient_id']

        conn = db_config.connect()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO Blood_delivery (Blood_bank_id, Patient_id)
                VALUES (%s, %s)
            """, (blood_bank_id, patient_id))
            conn.commit()
        except Exception as e:
            return f"<h3>Error: {e}</h3>"
        finally:
            cur.close()
            conn.close()

        return redirect('/view_blooddelivery')
    return render_template('add_blooddelivery.html')


@app.route('/view_blooddelivery')
def view_blooddelivery():
    conn = db_config.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Blood_delivery")
    blooddeliverys = cur.fetchall()
    conn.close()
    return render_template('view_blooddelivery.html', blooddeliverys=blooddeliverys)


if __name__ == '__main__':
    app.run(debug=True)
