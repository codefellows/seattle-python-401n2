import Header from './Header'

// const layoutStyle = {
//     margin: 20,
//     padding: 20,
//     border: '1px solid #DDD'
// }

export default function Layout(props) {
    return (
        <>
            <div>
                <Header />
                {props.children}
            </div>
            <style jsx>{`
                div {
                    margin: 20px;
                    padding: 20px;
                    border: 1px solid #DDD
                }
            `}</style>
        </>
    )
}
