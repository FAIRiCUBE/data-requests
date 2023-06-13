import ruamel.yaml
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


GH_TOKEN = "<github-token>"


def validate_document(document):
    keys = [
        'ID', 'Description', 'Project purpose',
        'Preferred Platform', 'Preferred Method', 'Axes', 'Cell type',
        'Null values', '(Meta) data Standards', 'APIs', 'Access control',
        'Responsible', 'Data Source', 'Data Preprocessing', 'Quality Control',
        'Documents & publications', 'License', 'Ownership', 'Personal Data',
        'Additional Information'
    ]
    document_keys = list(document.keys())

    return keys == document_keys or set(document_keys) - set(keys) == {'Target Platform'}


def insert_value(field, value_list, listed_fields, doc):

    if field in listed_fields:
        if len(value_list) == 1:
            doc[field] = value_list[0].split(", ")
        else:
            doc[field] = value_list
    else:
        doc[field] = "\n".join(value_list)


def yaml_builder(input_txt, out_yaml):
    values = []
    document = dict()
    temp_values = []
    list_fields = ['APIs', 'Null values', '(Meta) data Standards']

    response_lines = input_txt.splitlines()
    fields = []
    for index, i in enumerate(response_lines):

        if i != "\n" and i != '':
            st = i.strip("\n")
            st = st.strip(" ")
            st = st.replace("'", "")
            values.append(st)
    field = ''
    for index, value in enumerate(values):
        if type(value) == str and value.startswith('### '):

            field = values[index][4:]
            fields.append(field)

            if len(temp_values) > 0:
                temp_values = []
                fields.pop(0)
        else:
            value = value.replace("_No response_", "")
            temp_values.append(value)

        if index == len(values) - 1:
            document[field] = temp_values

        insert_value(field, temp_values, list_fields, document)
    if validate_document(document):

        with open(out_yaml, 'w') as file:
            yaml = ruamel.yaml.YAML()
            yaml.indent(sequence=3, offset=3)
            yaml.dump(document, file)
        file.close()


transport = RequestsHTTPTransport(
    url="https://api.github.com/graphql",
    headers={'Authorization': 'token ' + GH_TOKEN})

client = Client(transport=transport)

query_1 = gql(
        """
        query  {
            organization(login: \"FAIRiCUBE\") {
                repository(name: "data-requests") {
                    issues(last:100, states:OPEN) {
                        edges {
                            node {
                            title
                            body
                            }
                        }
                        }
                    }
                }
            }
        """
    )

issues = client.execute(query_1)['organization']['repository']['issues']['edges']
for index, issue in enumerate(issues):
    title = issue['node']['title'].split("]: ")[-1]
    yaml_builder(issue['node']['body'], f'./yaml/{title}.yaml')
