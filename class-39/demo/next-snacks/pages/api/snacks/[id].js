// placeholder API
export default (req, res) => {
    res.statusCode = 200

    const snacks = [
        { id: 1, name: 'Snickers', category: 'Candy' },
        { id: 2, name: 'Hummus', category: 'Savory' },
        { id: 3, name: 'Grapes', category: 'Fruit' },
        { id: 4, name: 'Steak', category: 'Meat' },
        { id: 5, name: 'Salami', category: 'Savory' },
    ]

    const snack = snacks[parseInt(req.query.id) - 1];

    res.json(snack);

  }
