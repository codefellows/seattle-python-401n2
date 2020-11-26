export default function SnackDetail(props) {
    return <h1>I am a single snack {props.snack.name}</h1>
}

export async function getServerSideProps(context) {
    const response = await fetch(`https://drf-snacks-api.herokuapp.com/api/v1/snacks/${context.params.id}`);
    const snack = await response.json();
    console.log('snack',snack)
    return {
        props: {
            snack
        }
    }
}
