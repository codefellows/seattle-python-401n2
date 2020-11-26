// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

export default (req, res) => {
  res.statusCode = 200
  res.json(
    [
        { id: 1, name: 'Snickers', category: 'Candy' },
        { id: 2, name: 'Hummus', category: 'Savory' },
        { id: 3, name: 'Grapes', category: 'Fruit' },
        { id: 4, name: 'Steak', category: 'Meat' },
        { id: 5, name: 'Salami', category: 'Savory' },
    ]
  )
}
