<template>
  <div id="schedule-game-info">
    <div id="header-info">
      <div id="back-button-container">
        <el-button
          size="medium"
          @click="backToScheduleClicked()">
          <i class="el-icon-d-arrow-left"></i>
          Back
        </el-button>
      </div>
      <div id="main-game-info">
        <div id="team-names">
          <div id="away-team"
            @click="teamClicked(localSelectedGame.awayTeamID)"
            :style="{'cursor': 'pointer'}">
            <ColorCircleTeamName
              :team="teamById(localSelectedGame.awayTeamID)"
              justifyContent="center"/>
          </div>
          <span id="vs-span">vs.</span>
          <div id="home-team"
            @click="teamClicked(localSelectedGame.homeTeamID)"
            :style="{'cursor': 'pointer'}">
            <ColorCircleTeamName
              :team="teamById(localSelectedGame.homeTeamID)"
              justifyContent="center"/>
          </div>
        </div>
        <div id="location-info">
          at {{ localSelectedGame.fieldName }}
        </div>
        <div
          id="date-time-info"
          v-if="selectedGame">
          {{ formatDate(localSelectedGame.gameTime.split(' ')[0]) }}
          at
          {{ formatTime(localSelectedGame.gameTime.split(' ')[1]) }}
        </div>
        <div
          id="cancelled-header"
          v-if="localSelectedGame.status === 'Cancelled'">
          CANCELLED
        </div>
      </div>
      <div id="game-actions-container">
        <el-button
          v-if="showCancelButton"
          size="medium"
          @click="cancelGameButtonClicked()"
          type="danger"
          plain>
          <i class="el-icon-circle-close-outline"></i>
          Cancel Game
        </el-button>
        <el-button
          v-if="showRescheduleButton"
          size="medium"
          @click="resechduleGameButtonClicked()">
          Reschedule Game
        </el-button>
        <el-button
          v-if="showSubmitGameSheetButton && !submitGameSheetVisible"
          :disabled="!bothRostersSubmited"
          size="medium"
          @click="submitGameSheetButtonClicked(true)">
          Submit Game Sheet
        </el-button>
      </div>
    </div>

    <div
      id="game-info-final-score"
      v-if="localSelectedGame.status === 'Final'">
      FINAL
    </div>

    <div
      class="roster-container"
      v-if="!submitGameSheetVisible && selectedGame.status === 'Scheduled'">
      <div class="away-team-roster-container">
        <TeamRosterContainer :team="teamById(localSelectedGame.awayTeamID)"/>
      </div>

      <div class="home-team-roster-container">
        <TeamRosterContainer :team="teamById(localSelectedGame.homeTeamID)"/>
      </div>
    </div>

    <div
      class="submit-game-sheet-ctonainer"
      v-else-if="submitGameSheetVisible && selectedGame.status === 'Scheduled'">
      <ScheduleGameSubmitGameSheet :callBackFunc="backToScheduleClicked"/>
    </div>

    <div
      class="final-game-sheet-ctonainer"
      v-else-if="selectedGame.status === 'Final'">
      <ScheduleGameFinalGameSheet/>
    </div>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import ColorCircleTeamName from '@/components/ColorCircleTeamName.vue';
import TeamRosterContainer from '@/components/TeamRosterContainer.vue';
import ScheduleGameSubmitGameSheet from '@/components/ScheduleGameSubmitGameSheet.vue';
import ScheduleGameFinalGameSheet from '@/components/ScheduleGameFinalGameSheet.vue';

export default {
  name: 'ScheduleGameInfo',
  data() {
    return {
      submitGameRosterVisible: false,
      submitRosterTeam: null,
      submitGameSheetVisible: false,
    };
  },
  components: {
    ColorCircleTeamName,
    TeamRosterContainer,
    ScheduleGameSubmitGameSheet,
    ScheduleGameFinalGameSheet,
  },
  computed: {
    ...mapGetters([
      'selectedGame',
      'teamById',
      'user',
      'selectedLeagueId',
      'gameRosters',
      'selectedGameId',
    ]),
    showCancelButton() {
      if (!this.user) {
        return false;
      }
      if (this.selectedGame.status === 'Cancelled') {
        return false;
      }
      const userType = this.user.userType;
      switch (userType) {
        case ('Admin'):
          return true;
        case ('Coordinator'):
          return (this.selectedLeague || {}).managerID === this.user.userID;
        default:
          return false;
      }
    },
    showRescheduleButton() {
      if (!this.user) {
        return false;
      }
      if (this.selectedGame.status !== 'Cancelled') {
        return false;
      }
      const userType = this.user.userType;
      switch (userType) {
        case ('Admin'):
          return true;
        case ('Coordinator'):
          return (this.selectedLeague || {}).managerID === this.user.userID;
        default:
          return false;
      }
    },
    showSubmitGameSheetButton() {
      if (!this.user) {
        return false;
      }
      if (this.selectedGame.status === 'Cancelled') {
        return false;
      }
      if (this.selectedGame.status === 'Final') {
        return false;
      }
      const userType = this.user.userType;
      switch (userType) {
        case ('Referee'):
          return true;
        default:
          return false;
      }
    },
    bothRostersSubmited() {
      const homeTeamRoster = this.fullGameRoster.filter(player => {
        return player.teamID === this.selectedGame.homeTeamID;
      });
      const awayTeamRoster = this.fullGameRoster.filter(player => {
        return player.teamID === this.selectedGame.awayTeamID;
      });
      return homeTeamRoster.length > 0 && awayTeamRoster.length > 0;
    },
    fullGameRoster() {
      const gameRosterObj = this.gameRosters.find(gameRoster => {
        return gameRoster.gameID === this.selectedGameId;
      });
      return gameRosterObj ? gameRosterObj.players : [];
    },
    localSelectedGame() {
      return this.selectedGame || {};
    },
  },
  methods: {
    ...mapActions([
      'editGame',
      'setSelectedTeamId',
    ]),
    backToScheduleClicked() {
      if (this.submitGameSheetVisible) {
        this.submitGameSheetVisible = false;
      } else {
        this.$router.push('/schedule');
      }
    },
    formatDate(mDate) {
      const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
      const tempDate = mDate.split('-');
      return `${months[Number(tempDate[1]) - 1]} ${tempDate[2]}, ${tempDate[0]}`;
    },
    formatTime(mTime) {
      // Check correct time format and split into components
      let time = mTime.toString().match(/^([01]\d|2[0-3])(:)([0-5]\d)(:[0-5]\d)?$/) || [mTime];
      time[4] = ' ';// Change seconds to just a space
      if (time.length > 1) { // If time format correct
        time = time.slice(1); // Remove full string match value
        time[5] = +time[0] < 12 ? 'AM' : 'PM'; // Set AM/PM
        time[0] = +time[0] % 12 || 12; // Adjust hours
      }
      return time.join(''); // return adjusted time or original string
    },
    cancelGameButtonClicked() {
      this.$confirm('Are you sure you want to cancel this game?', 'Confirm Game Cancellation', {
        confirmButtonText: 'Cancel Game',
        cancelButtonText: 'No',
        type: 'warning',
      }).then(() => {
        const updateGameObj = { ...this.selectedGame };
        updateGameObj.status = 'Cancelled';
        this.editGame(updateGameObj).then((response) => {
          if (response.retVal) {
            this.$message({
              message: 'Game Cancelled',
              center: true,
            });
          } else {
            this.$message.error(response.retMsg);
          }
        });
      }).catch(() => {
      });
    },
    resechduleGameButtonClicked() {
      this.$router.push('/schedule/game/reschedule');
    },
    teamClicked(id) {
      this.setSelectedTeamId(id);
      this.$router.push(`/teams/${id}`);
    },
    submitGameSheetButtonClicked(val) {
      this.submitGameSheetVisible = val;
    },
  },
  watch: {
    selectedLeagueId() {
      this.$router.push('/schedule');
    },
  },
  mounted() {
    if (!this.selectedGame) {
      this.$router.push('/schedule');
    }
  },
};
</script>

<style lang="scss">
@import '@/style/global.scss';

#schedule-game-info{
  display: flex;
  flex-direction: column;
  margin: 8px 16px;

  #header-info{
    display: flex;
    flex-direction: row;
    justify-content: space-between;

    #back-button-container{

    }

    #main-game-info{
      display: flex;
      flex-direction: column;

      #team-names{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        font-size: 1.4rem;
        font-weight: bold;

        #vs-span{
          margin: 0px 8px;
        }

        #away-team,
        #home-team{
          transition: 0.2s;

          &:hover{
            color: lighten($DARK_TEXT, 30%);
          }
        }
      }

      #cancelled-header{
        font-weight: bold;
        color: $CANCELLED_RED;
      }
    }

    #game-actions-container{
      min-width: 93px;
    }
  }

  #game-info-final-score{
    font-size: 1.2rem;
    font-weight: bold;
    margin-top: 8px;
  }

  .roster-container{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    flex-wrap: wrap;

    .away-team-roster-container,
    .home-team-roster-container{
      width: calc(45%);
    }
  }

  .submit-roster-container{
    display: flex;
    justify-content: center;
  }
}
</style>
