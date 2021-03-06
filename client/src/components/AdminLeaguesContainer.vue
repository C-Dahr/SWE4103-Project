<template>
  <div id="admin-leagues-container">
    <div id="title-container">
    </div>
    <div id="create-league-button-container">
      <el-button
      @click="leagueCreateClicked()"
      type="primary">Create New League</el-button>
    </div>
    <div id="leagues-table-container">
      <el-table
        :data="formatLeagues"
        :default-sort = "{prop: 'id', order: 'ascending'}"
        stripe
        style="width: 100%">
        <el-table-column
          prop="leagueID"
          sortable
          width="110px"
          label="League ID">
        </el-table-column>
        <el-table-column
          prop="leagueName"
          sortable
          :show-overflow-tooltip="true"
          label="Name">
        </el-table-column>
        <el-table-column
          prop="season"
          sortable
          :show-overflow-tooltip="true"
          label="Season">
        </el-table-column>
        <el-table-column
          prop="pointScheme"
          sortable
          :show-overflow-tooltip="true"
          label="Point Scheme">
        </el-table-column>
        <el-table-column
          prop="managerName"
          sortable
          :show-overflow-tooltip="true"
          label="Coordinator">
        </el-table-column>
        <el-table-column
          label="Action">
          <template slot-scope="scope">
            <el-button
            icon="el-icon-edit"
            size="mini"
            :disabled="actionEditDisabled(scope.row)"
            @click='leagueEditClicked(scope.row.leagueID)'>
            </el-button>
            <el-button
            icon="el-icon-delete"
            size="mini"
            :disabled="actionDeleteDisabled(scope.row)"
            @click="leagueDeleteClicked(scope.row.leagueID, scope.row.leagueName)">
            </el-button>
          </template>
        </el-table-column>

      </el-table>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'AdminLeaguesContainer',
  data() {
    return {

    };
  },
  computed: {
    ...mapGetters([
      'leagues',
      'leagueById',
      'userById',
      'user',
    ]),
    formatLeagues() {
      const formattedLeagues = this.leagues.map((league) => {
        const manager = this.userById(league.managerID);
        const managerNameIn = manager ? `${manager.firstName} ${manager.lastName}` : 'None';
        return {
          ...league,
          managerName: managerNameIn,
        };
      });
      return formattedLeagues;
    },
    curRoute() {
      return this.$route.name;
    },
  },
  methods: {
    ...mapActions([
      'deleteLeague',
      'setEditedLeague',
      'setEditLeagueModalVisible',
    ]),
    actionEditDisabled(leagueObj) {
      if (!this.user) {
        return true;
      }
      switch (this.user.userType) {
        case ('Admin'): {
          return false;
        }
        case ('Coordinator'): {
          return leagueObj.managerID !== this.user.userID;
        }
        default:
          return true;
      }
    },
    actionDeleteDisabled() {
      if (!this.user) {
        return true;
      }
      switch (this.user.userType) {
        case ('Admin'): {
          return false;
        }
        case ('Coordinator'): {
          return true;
        }
        default:
          return true;
      }
    },
    leagueCreateClicked() {
      this.$router.push('/admin/leagues/create');
    },
    leagueEditClicked(index) {
      this.setEditedLeague(index);
      this.setEditLeagueModalVisible(true);
    },
    leagueDeleteClicked(id, name) {
      this.$confirm(`Are you sure you want to delete ${name}? (This will also delete all associated teams and players)`, 'Confirm League Deletion', {
        confirmButtonText: 'Delete League',
        cancelButtonText: 'Cancel',
        type: 'warning',
      }).then(() => {
        this.deleteLeague(this.leagueById(id)).then((response) => {
          if (response.retVal) {
            this.$message({
              message: `Deleted ${name}`,
              center: true,
            });
          } else {
            this.$message.error('Error deleting');
          }
          this.$router.push('/admin/leagues');
        });
      }).catch(() => {
      });
    },
  },
};

</script>

<style lang="scss" scoped>
@import '@/style/global.scss';
#admin-leagues-container{

  #create-league-button-container{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-end;
    height: 61px;
    transition: 0.3s;
  }
  .asd {
    background:rgba(0,0,0,0);
    border: 1px solid rgba(0,0,0,0);
    width: 20%;
  }
}
</style>
