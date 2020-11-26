import Link from 'next/link'
import Nav from '../components/Nav'

function Home(props) {
    return (
        <div className="container">
            <Nav />
            <h1>Home</h1>
            <ul>
    {props.snacks.map(snack => <SnackItem snack={snack} />)}
            </ul>

        <style jsx>{`
            .container {
                text-align: center;
            }
        `}
        </style>

        <style jsx global>{`
                html,
                body {
                padding: 0;
                margin: 0;
                font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto,
                    Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue,
                    sans-serif;
                }

                * {
                box-sizing: border-box;
                }
            `}</style>

        </div>
    )
}

function SnackItem(props) {
    return (
        <li key={props.snack.id}>
            <Link href="/snacks/[id]" as={`/snacks/${props.snack.id}`}>
            <a>
                {props.snack.name}
            </a>
            </Link>
            </li>
    )
}

export default Home

export async function getStaticProps() {

    const url = 'https://drf-snacks-api.herokuapp.com/api/v1/snacks/'; // for production use 'http://production-site/api/snacks'
    const response = await fetch(url);
    const snacks = await response.json();

    return {
      props: {
          snacks : snacks,
      },
    }
  }
