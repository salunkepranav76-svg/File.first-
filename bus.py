from flask import Flask, render_template, request

app = Flask(__name__)

# Sample routes with prices
routes = {
    "Delhi to Mumbai": 1200,
    "Hyderabad to Bangalore": 800,
    "Chennai to Kochi": 900,
    "Pune to Goa": 700,
    "Jaipur to Agra": 600
}

tickets = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        gender = request.form['gender']
        route = request.form['route']
        date = request.form['date']
        price = routes.get(route, 0)

        ticket = {
            'name': name,
            'mobile': mobile,
            'gender': gender,
            'route': route,
            'date': date,
            'price': price
        }
        tickets.append(ticket)
        message = "Ticket Confirmed"
        return render_template('index.html', message=message, routes=routes, tickets=tickets, latest_ticket=ticket)

    return render_template('index.html', routes=routes, tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True)