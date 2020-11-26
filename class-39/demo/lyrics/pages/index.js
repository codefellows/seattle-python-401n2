import axios from 'axios';
import Layout from '../components/MyLayout';

export default ({ lyrics }) => (
    <Layout>
        <h1>King of America</h1>
        <h2>Elvis Costello</h2>
        <div>{lyrics}</div>
        <style jsx>{`
            div {
                white-space: pre-wrap;
            }
        `}</style>
    </Layout>
)

export async function getStaticProps() {

    const response = await axios.get('https://api.lyrics.ovh/v1/elvis%20costello/brilliant%20mistake');

    const lyrics = response.data.lyrics;

    return {
        props: { lyrics }
    }
}
