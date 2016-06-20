# Checkout
Python 3.5.1

An exercise according to this task:

In a normal supermarket, things are
identified using Stock Keeping Units, or SKUs. In our store, we’ll use
individual letters of the alphabet (A, B, C, and so on). Our goods are priced
individually. In addition, some items are multipriced: buy n of them, and
they’ll cost you y cents.  Today we are selling goods A, B, C, D and E by the
following prices: “A costs 50 cents,” “three A cost $1.30,” “B costs 30 cents,
two B cost 45 cents,” “$1.99 per kg of C,” and “D costs $1.20, E costs $0.90,
buy two D, get one E free.” Our checkout accepts items in any order, so that if
we scan a B, an A, and another B, we’ll recognize the two B’s and price them at
45 (for a total price so far of 95).

Implement checkout as an HTML-form with one select field with options A-E and
text input for kg's in case C is chosen. User selects one of the goods he wants
to buy and submits the form, current total is calculated according to the prices
above stored in DB and displayed to the user. User can choose another good. You
have 60 mins.

Note: time is hard limited, thus it is better to do task in time in suboptimal
way than to not do it in time in a better way.

## Usage 
```
# python 3.5.1
python -m venv checkout
./checkout/bin/pip install -r requirements.txt
./checkout/bin/python server.py
```
Now you can open your browser and go to `localhost:8000`
