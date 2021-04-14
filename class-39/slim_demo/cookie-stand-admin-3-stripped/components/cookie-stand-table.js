import { hours } from '../data'

export default function CookieStandTable({ stands, onDelete }) {

    return (
        <Table>
            <thead>
                <tr>

                    <TH>Location</TH>
                    {hours.map(slot => (
                        <TH key={slot}>{slot}</TH>
                    ))}
                    <TH>Totals</TH>
                </tr>
            </thead>
            <tbody>
                {stands.map((stand, i) => {

                    return (
                        <tr key={stand.id}>

                            <TH>
                                <div>

                                    <p>{stand.location}</p>

                                    <span onClick={() => onDelete(stand)}>X</span>
                                </div>
                            </TH>

                            {stand.cookiesEachHour.map((amt, i) => (
                                <TD key={i}>
                                    {amt}
                                </TD>
                            ))}
                            <TD>{stand.totalDailyCookies}</TD>
                        </tr>
                    )
                })}
            </tbody>
            <tfoot>
                <tr>
                    <TH>Totals</TH>
                    {hours.map((_, i) => {
                        const amt = stands.reduce((acc, cur) => acc + cur.cookiesEachHour[i], 0);
                        return <TD key={'amt' + i}>{amt}</TD>
                    })}
                    <TD>{stands.reduce((acc, cur) => acc + cur.totalDailyCookies, 0)}</TD>
                </tr>
            </tfoot>
        </Table>

    );
}

function Table({ children }) {
    return (
        <table>
            {children}
        </table>
    );
}
function TH({ children }) {
    return (
        <th>{children}</th>
    )
}

function TD({ children }) {
    return (
        <td>{children}</td>
    )
}
