import axios from 'axios';
import Layout from '../../components/MyLayout';

const Post = props => (
    <Layout>
        <h1>{props.show.name}</h1>
        <p>{props.show.summary.replace(/<[/]?[pb]>/g, '')}</p>
        {props.show.image ? <img src={props.show.image.medium} /> : null}
    </Layout>
)

Post.getInitialProps = async function (context) {
    const id = context.query.id;
    const response = await axios.get(`https://api.tvmaze.com/shows/${id}`)
    return { show: response.data }
}

export default Post;


