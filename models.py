import glob
import os
import pandas as pd

class User:

    @classmethod
    def materialize_data(self, directory: str) -> pd.DataFrame:
        filenames = glob.glob(os.path.join(directory, 'users*.json'))
        df = [pd.read_json(filename) for filename in filenames]
        assert len(df) > 0

        usersDf = pd.concat(df, ignore_index=True, sort=True) if len(df) > 1 else df[0]
        usersDf = usersDf.astype({"active":             str})
        usersDf = usersDf.astype({"verified":           str})
        usersDf = usersDf.astype({"shared":             str})
        usersDf = usersDf.astype({"organization_id":    str})

        usersDf = usersDf.apply(lambda x: x.astype(str).str.lower())
        return usersDf

class Organization:

    @classmethod
    def materialize_data(self, directory: str) -> pd.DataFrame:
        filenames = glob.glob(os.path.join(directory, 'organizations*.json'))
        df = [pd.read_json(filename) for filename in filenames]
        assert len(df) > 0

        organizationsDF = pd.concat(df, ignore_index=True, sort=True) if len(df) > 1 else df[0]
        organizationsDF = organizationsDF.astype({"shared_tickets":   str})

        organizationsDF = organizationsDF.apply(lambda x: x.astype(str).str.lower())
        return organizationsDF

class Tickets:

    @classmethod
    def materialize_data(self, directory: str) -> pd.DataFrame:
        filenames = glob.glob(os.path.join(directory, 'tickets*.json'))
        df = [pd.read_json(filename) for filename in filenames]
        assert len(df) > 0

        ticketsDF = pd.concat(df, ignore_index=True, sort=True) if len(df) > 1 else df[0]
        ticketsDF = ticketsDF.astype({"submitter_id":       str})
        ticketsDF = ticketsDF.astype({"assignee_id":        str})
        ticketsDF = ticketsDF.astype({"organization_id":    str})
        ticketsDF = ticketsDF.astype({"has_incidents":      str})

        ticketsDF = ticketsDF.apply(lambda x: x.astype(str).str.lower())
        return ticketsDF
