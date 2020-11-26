import axios from 'axios';
import Link from 'next/link';

import Layout from '../components/MyLayout';

const Index = props => (
    <Layout>
        <h1>Batman TV Shows</h1>
        <ul>
            {props.shows.map(show => (
                <li key={show.id}>
                    <Link href="/p/[id]" as={`/p/${show.id}`}>
                        <a>
                            {show.name}
                        </a>
                    </Link>
                </li>
            ))}

        </ul>
    </Layout>
)

// Index.getInitialProps = async function () {
export async function getStaticProps() {
    const response = await axios.get('https://api.tvmaze.com/search/shows?q=batman');
    console.log('Show data fetched. Count: ', response.data.length);
    const showData = {
        shows: response.data.map(item => item.show)
    }
    // return showData;
    return {
        props: showData
    }
}

export default Index
